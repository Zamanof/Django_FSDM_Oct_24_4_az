from django.shortcuts import render, redirect

from forms_example.forms import ContactForm, FeedbackForm, NoteDraftForm


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("success")
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def feedback_view(request):
    form = FeedbackForm(request.POST or None)
    submitted_data = None

    if request.method == 'POST':
        submitted_data = form.cleaned_data
    return render(request, 'feedback.html', {'form': form, 'submitted_data': submitted_data})


def note_draft(request):
    if request.method == 'POST':
        form = NoteDraftForm(request.POST)
        if form.is_valid():
            return redirect("feedback_page")
    else:
        form = NoteDraftForm()
    return render(request, 'note_draft.html', {'form': form})