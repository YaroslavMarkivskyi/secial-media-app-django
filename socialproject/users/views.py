from django.shortcuts import render
from .forms import LoginForm
# Create your views here.


def user_login(request):
    form = LoginForm()
    return(request, 'users/login.html', {'form': form})
