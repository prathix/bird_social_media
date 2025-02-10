from django.shortcuts import render, redirect
from .models import Post
from django.contrib .auth.forms import UserCreationForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", {'posts': posts})

def registration_form(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "app/auth.html", {"form": form})