from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request, "event_manager/base.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  # Make sure this redirects to the homepage
    form = UserCreationForm()
    return render(request, "event_manager/register.html", {"form": form})