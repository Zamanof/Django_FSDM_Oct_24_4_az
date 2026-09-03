from django import forms

from notes.models import Note


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter your message", "class": "form-control"}),
    )


from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tags']

        labels = {
            'title': 'Title',
            'content': 'Content',
            'category': 'Category',
            'tags': 'Tags',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title',
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your note...',
                'rows': 5,
            }),

            'category': forms.Select(attrs={
                'class': 'form-select',
            }),

            'tags': forms.SelectMultiple(attrs={
                'class': 'form-select',
            }),
        }

    def clean_title(self) -> str:
        title = self.cleaned_data['title'].strip()

        if title.lower().startswith("test"):
            raise forms.ValidationError(
                "Title must not start with 'test'."
            )

        return title