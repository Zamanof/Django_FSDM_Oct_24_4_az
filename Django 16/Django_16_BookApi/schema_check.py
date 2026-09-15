from pydantic import ValidationError

from shcemas import BookCreate, AuthorCreate, UserRegister


def show(title, data, schema):
    print(f"\n=== {title} ===")
    try:
        obj = schema.model_validate(data)
        print(f"Ok: {obj.model_dump()}")
    except ValidationError as e:
        print(f"Validation error: {e}")



if __name__ == "__main__":
    show(
        "Book ok",
        {"title":"CLR via C#","pages":852, "author_id":1},
        BookCreate)

    show(
        "Book with 0 pages",
        {"title": "CLR via C#", "pages": 0, "author_id": 1},
        BookCreate)

    show(
        "Author ok",
        {"name": "Jeffrey Richter"},
        AuthorCreate)

    show(
        "Author  empty name",
        {"name": ""},
        AuthorCreate)

    show(
        "Short Password",
        {"email": "a@b.com", "password": "P@ss"},
        UserRegister)
