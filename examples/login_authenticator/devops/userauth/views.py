from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def homepage(request):
    return render(request, 'userauth/homepage.html')

def register_user(request):
    if request.method == 'POST':
        registartion_form = UserCreationForm(request.POST)
        if registartion_form.is_valid():
            new_user = registartion_form.save()
            login(request, new_user)
            return redirect('homepage')
    else:
        registartion_form = UserCreationForm()
    return render(request, 'userauth/register.html', {'form': registartion_form})

def login_user(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return render(request, 'userauth/welcome.html', {'user': user})
    else:
        login_form = AuthenticationForm()
    return render(request, 'userauth/login.html', {'form': login_form})

def logout_user(request):
    logout(request)
    return redirect('homepage')