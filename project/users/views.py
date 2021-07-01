
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.models import User


def login_views(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("success")
            login(request, user)
            return redirect('/index')
        else:
            print("fail")

    return render(request, "users/login.html")

def index(request):
    return render(request, "users/index.html")

def search(request):
    return render(request, "users/search.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']

        user = User.objects.create_user(username, password, name)
        user.email = email
        user.save()
        return redirect('/index')
    return render(request, 'users/register.html')

def logout_views(request):
    logout(request)
    return redirect("user:index")

def find(request):
    if request.method == "POST":
        email = request.POST["email"]

    return render(request, "users/find.html")

def blog(request):

    return render(request, "users/blog_list.html")
