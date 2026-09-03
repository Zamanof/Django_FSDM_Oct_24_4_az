from django import forms

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


class NoteForm(forms.Form):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('work', 'Work'),
        ('personal', 'Personal'),
    ]
    title = forms.CharField(
        label="Title",
        min_length=5,
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Enter your title", "class": "form-control"}),
    )
    content = forms.CharField(
        label="Content",
        min_length=20,
        widget=forms.Textarea(attrs={"placeholder": "Enter your content", "rows": 4, "class": "form-control"}),
    )
    tags = forms.CharField(
        label="Tags",
        widget=forms.TextInput(attrs={"placeholder": "Enter your tags", "class": "form-control"}),
    )
    category = forms.ChoiceField(
        label="Category",
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
