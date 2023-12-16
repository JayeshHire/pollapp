from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

def login_form(request):
    return render(request, "registration/login_form.html")


def login_view(request):
    username = request.POST["username"]
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return render(request, 'registration/success.html')
    else:
        return render(request, 
                      "<h1> Check your login credentials<h1>")