from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.changed_data
            user = authenticate(request,
                         username=data['username'],
                         password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("user authenticated")
            else:
                return HttpResponse("user doesn't authenticated")

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def index(request):
    return render(request, 'users/index.html')