from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')


class FeedbackForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, min_length=20)



class NoteDraftForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    secret_word = forms.CharField()
    confirm_secret_word = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long")
        banned_words = ["spam", "virus", "niga"]
        if any(word in title for word in banned_words):
            raise forms.ValidationError(f"Title must not contain any of the following words: {banned_words}")
        return title

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get('secret_word')
        second = cleaned_data.get('confirm_secret_word')
        if first and second and first != second:
            raise forms.ValidationError(f"Secret word and confirm secret word must have the same value")
        return cleaned_data