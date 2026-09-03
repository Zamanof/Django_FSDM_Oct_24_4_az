from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView
from pyexpat.errors import messages

from .forms import ContactForm, NoteForm
from .models import Note


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
    notes = Note.objects.select_related("author", 'category').prefetch_related('tags').all()
    return render(request, 'notes/notes_list.html', {"notes": notes})


def note_detail(request: HttpRequest, note_id:int) :
    pass


def note_create(request: HttpRequest) :
    if request.method == "POST" :
        form = NoteForm(request.POST)
        if form.is_valid() :
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, "Note created successfully")
            return redirect("notes:note_detail", pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {"form": form, 'mode':'create'})

def note_edit(request: HttpRequest, note_id: int) :
    pass


def note_delete(request: HttpRequest, note_id: int) :
   pass


def contact_form(request: HttpRequest):
    pass