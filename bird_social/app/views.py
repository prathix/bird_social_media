from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", {'posts': posts})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('home')  # Redirect to home or another page after signup
    else:
        form = SignUpForm()
    
    # Render the correct template
    return render(request, 'app/auth.html', {'signup_form': form, 'form_type': 'signup'})