from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", max_length=100, min_length=3)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="Username or email",
        max_length=100,
        min_length=3,
    widget=forms.TextInput(attrs={"placeholder": "Username or email"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )