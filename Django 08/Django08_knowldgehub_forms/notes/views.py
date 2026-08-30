from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView

from . import data
from .forms import ContactForm


def home(request: HttpRequest) :
    return render(request, 'notes/home.html', {
        "page_title": "Knowledge Hub",
        'welcome_text': "Welcome to Knowledge Hub",
    })


class AboutPageView(TemplateView):
    template_name = 'notes/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_name'] = "Knowledge Hub Super Pupper"
        context['author'] = "Nadir Zamanov"
        context['description'] = "Knowledge Hub Super Pupper"
        return context

def notes_list(request: HttpRequest) :
    notes = data.list_notes()
    return render(request, 'notes/notes_list.html', {"notes": notes})


def note_detail(request: HttpRequest, note_id:int) :
    note = data.get_note(note_id)
    return render(request, 'notes/note_detail.html', {"note": note})


def note_create(request: HttpRequest) :
    if request.method == "POST":
        title = request.POST.get("title", "")
        note_body = request.POST.get("body", "")
        tag = request.POST.get("tag", "")
        category = request.POST.get("category", "")

    return render(request, 'notes/note_create.html')

def note_edit(request: HttpRequest, note_id: int) :
    note = data.get_note(note_id)


    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        tags = request.POST.get("tags", "").split()
        category= request.POST.get("category", "")
        data.update_note(
            note_id,
            title=title,
            content=content,
            tags=tags,
            category=category)
        return redirect('notes_list')

    return render(request, 'notes/note_edit.html', {"note": note, "note_id": note_id})


def note_delete(request: HttpRequest, note_id: int) :
    note = data.get_note(note_id)


    if request.method == "POST":
        data.delete_note(note_id)
        return redirect("notes_list")

    return render(request, 'notes/note_delete.html', {"note": note})


def contact_form(request: HttpRequest):
    form = ContactForm()
    return render(request, "notes/contact.html", {"form": form})