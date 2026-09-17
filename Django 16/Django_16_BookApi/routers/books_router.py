from typing import Optional

from fastapi import Depends, HTTPException, Query
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from deps import require_roles, get_db
from helpers import paginate
from models import Role, Author, Book
from shcemas import BookOut, BookCreate, BookUpdate

router = APIRouter(prefix="/api/books", tags=["books"])

@router.post(
    "/",
    response_model=BookOut,
    dependencies=[Depends(require_roles(Role.admin))],
    status_code=status.HTTP_200_OK,
)
def create_book(
        payload: BookCreate,
        db: Session=Depends(get_db)
):
    author = db.query(Author).filter_by(id=payload.author_id).first()
    if author is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Author not found")

    book = Book(
        title=payload.title.strip(),
        pages=payload.pages,
        author_id=payload.author_id,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get(
    "/",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
def list_books(
        q: Optional[str] = Query(None),
        order: str = Query("name"),
        page: int = Query(1, ge=1),
        size: int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db)
):
    query = db.query(Book)

    if q:
        query = query.filter(Book.title.ilike(f"%{q}%"))

    allowed = {'title', 'pages', 'id'}

    if order.lstrip('-') not in allowed:
        order = 'title'

    col = getattr(Book, order.lstrip('-'))

    if order.startswith('-'):
        col = col.desc()
    query = query.order_by(col)

    data = paginate(query, page=page, size=size)
    data['results'] = [BookOut.model_validate(b) for b in data['results']]
    return data


@router.get(
    "/{book_id}",
    response_model=BookOut,
    status_code=status.HTTP_200_OK,
)
def get_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    book = db.query(Book).filter_by(id=book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@router.patch(
    "/{book_id}",
    response_model=BookUpdate,
    dependencies=[Depends(require_roles(Role.admin))],
    status_code=status.HTTP_200_OK,
)
def update_book(
        book_id: int,
        payload: BookUpdate,
        db: Session = Depends(get_db)
):
    book = db.query(Book).filter_by(id=book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    if payload.title is not None:
        book.title = payload.title.strip()
    if payload.pages is not None:
        book.pages = payload.pages
    if payload.author_id is not None:
        author = db.query(Author).filter_by(id=payload.author_id).first()
        if author is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
        book.author_id = payload.author_id

    db.commit()
    db.refresh(book)
    return book


@router.delete(
    "/{book_id}",
    dependencies=[Depends(require_roles(Role.admin))],
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    book = db.query(Book).filter_by(id=book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()
    return None