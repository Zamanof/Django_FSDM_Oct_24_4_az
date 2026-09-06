from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, "User created successfully")
            return redirect('accounts:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username_or_email'].strip()
            password = form.cleaned_data['password']

            user = authenticate(request, username=identifier, password=password)
            if user is None:
                User = get_user_model()
                try:
                    candidate = User.objects.get(email__iexact=identifier)
                except User.DoesNotExist:
                    candidate = None
                if candidate is not None:
                    user = authenticate(request, username=identifier, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "User logged in")

                return redirect('accounts:dashboard')
            form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_success(request):
    return render(
        request,
        'accounts/register_success.html',
        {'username': request.session['registered_user']})

def dashboard_view(request):
    User = get_user_model()
    notes_total = 0
    if request.user.is_authenticated:
        notes_total = request.user.notes.count()
    return render(
        request,
        'accounts/dashboard.html',
        {"notes_total": notes_total,
         "users_total": User.objects.count()}
    )

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "User logged out")
        return redirect('accounts:dashboard')
    return redirect('home')