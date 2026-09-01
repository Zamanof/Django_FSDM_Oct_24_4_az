from django.shortcuts import render, redirect

from accounts.forms import RegisterForm


# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            request.session['registered_user'] = form.cleaned_data['username']
            return redirect('accounts:register_success')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    pass

def register_success(request):
    pass

def dashboard_view(request):
    pass
