from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView

from . import data
from .forms import ContactForm, NoteForm


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
    get_note = data.get_note(note_id)
    note = {
        'id': note_id,
        "content": get_note["content"],
        "category": get_note["category"],
        "tags": ' '.join(get_note["tags"]),
        'title': get_note["title"],
        "created_at": get_note["created_at"],
    }

    return render(request, 'notes/note_detail.html', {"note": note})


def note_create(request: HttpRequest) :
    if request.method == "POST" :
        form = NoteForm(request.POST)
        if form.is_valid() :
            notes = request.session.get('notes', [])
            notes.append(
                {
                    'title': form.cleaned_data['title'],
                    'content': form.cleaned_data['content'],
                    'category': form.cleaned_data['category'],
                    'tags': form.cleaned_data['tags'],
                }
            )
            request.session['notes'] = notes
            data.create_note(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=form.cleaned_data['category'],
                tags=form.cleaned_data['tags'].split(),
            )
            return redirect('notes:notes_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_create.html', {"form": form})

def note_edit(request: HttpRequest, note_id: int) :
    note = data.get_note(note_id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid() :
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            category= form.cleaned_data['category']
            data.update_note(
            note_id,
            title=title,
            content=content,
            tags=tags.split(),
            category=category)
        return redirect('notes:notes_list')
    else:
        form = NoteForm(initial={
            'title': note['title'],
            'content': note['content'],
            'tags': " ".join(note['tags']),
            'category': note['category']})

    return render(request, 'notes/note_edit.html', {"note": note, "note_id": note_id, 'form':form})


def note_delete(request: HttpRequest, note_id: int) :
    note = data.get_note(note_id)


    if request.method == "POST":
        data.delete_note(note_id)
        return redirect("notes:notes_list")

    return render(request, 'notes/note_delete.html', {"note": note})


def contact_form(request: HttpRequest):
    form = ContactForm()
    return render(request, "notes/contact.html", {"form": form})