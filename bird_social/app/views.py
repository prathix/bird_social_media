from django.shortcuts import render
from .models import Post
from django.contrib .auth.forms import UserCreationForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", {'posts': posts})

def registration_form(request):
    form = UserCreationForm
    return render(request, "app/auth.html", {"form": form})