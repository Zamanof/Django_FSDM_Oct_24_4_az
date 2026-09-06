from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.views.generic import TemplateView

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

@login_required
def note_detail(request: HttpRequest, note_id:int) :
    note = get_object_or_404(
        Note.objects.select_related("author", 'category').prefetch_related('tags'),
        pk = note_id
    )
    return render(request, 'notes/note_detail.html', {"note": note})

@login_required
def note_create(request: HttpRequest) :
    if request.method == "POST" :
        form = NoteForm(request.POST)
        if form.is_valid() :
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, "Note created successfully")
            return redirect("notes:note_detail", note_id=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {"form": form, 'mode':'create'})


@login_required
def note_edit(request: HttpRequest, note_id: int) :
    note = get_object_or_404(Note, pk=note_id)
    if note.author_id != request.user.id :
        return HttpResponseForbidden('You are not authorized to edit this note')

    if request.method == "POST" :
        form = NoteForm(request.POST, instance=note)
        if form.is_valid() :
            form.save()
            return redirect("notes:note_detail", note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {"form": form, 'mode':'edit', 'note': note})


@login_required
def note_delete(request: HttpRequest, note_id: int) :
   note = get_object_or_404(Note, pk=note_id)
   if note.author_id != request.user.id :
       return HttpResponseForbidden('You are not authorized to delete this note')
   if request.method == "POST" :
       note.delete()
       messages.success(request, "Note deleted successfully")
       return redirect("notes:notes_list")
   return render(request, 'notes/note_delete.html', {"note": note})


def contact_form(request: HttpRequest):
    pass