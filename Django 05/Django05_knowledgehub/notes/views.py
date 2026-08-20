from django.utils.html import escape
from django.urls import reverse
from django.http import HttpResponse, HttpRequest

from . import data

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("KnowledgeHub Home Page")

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("KnowledgeHub About Page")

def notes_list(request: HttpRequest) -> HttpResponse:
    items:list[str] = []
    for note in data.list_notes():
        url = reverse("notes_detail", kwargs={"note_id": note["id"]})
        items.append(f"<li><a href='{escape(url)}'>{note['title']}</a></li>")
    body = (
        f"""
            <h1>KnowledgeHub Notes List</h1>
            <ul>
                {"".join(items)}
            </ul>
            <p>
                <a href="{escape(reverse('home'))}">Home Page</a>
            </p>    
        """
    )
    return HttpResponse(body)


def notes_detail(request: HttpRequest, note_id:int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse(f"Note id={note_id} not found")

    body = (
        f"""
            <h1>{escape(note['title'])}</h1>
            <p>{escape(note['body'])}</p>
            <p>
                <a href="{escape(reverse('notes_list'))}">Return to Notes List</a>
            </p>
        """
    )
    return HttpResponse(body)
