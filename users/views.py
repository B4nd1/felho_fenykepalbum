from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("images:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html",
                  {"form": form})
