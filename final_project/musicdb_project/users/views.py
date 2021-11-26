from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from users.models import UserEntity

# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now being redirected to home page!")
            return redirect("users:profile")
        messages.error(request, "Registration was unsuccessful. Invalid information provided.")
    form = NewUserForm()
    return render(request,"register.html", context={"register_form":form})

def profile(request, pk):
    user_info = UserEntity.objects.get(user_id=pk)
    user_data = {
        "user_detail" : user_info
    }
    return render(request, 'profile.html', user_data)
