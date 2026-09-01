from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows":4, 'placeholder':'Enter your message'}),)


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
        widget=forms.TextInput(attrs={'placeholder':'Enter your title'}),
    )
    content = forms.CharField(
        label="Content",
        min_length=20,
        widget=forms.Textarea(attrs={'placeholder':'Enter your content','rows':4}),
    )
    tags = forms.CharField(label="Tags", widget=forms.TextInput(attrs={'placeholder':'Enter your tags'}))
    category = forms.ChoiceField(label="Category", choices=CATEGORY_CHOICES)