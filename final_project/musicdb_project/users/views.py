from django.shortcuts import render, redirect
from .forms import NewUserForm, UserEntityForm
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
            return redirect("profile")
        messages.error(request, "Registration was unsuccessful. Invalid information provided.")
    form = NewUserForm()
    return render(request,"register.html", context={"register_form":form})

def display_profile(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    if request.user != user:
        return HttpResponseForbidden()

    if request.method == "GET":
        data = {
            "user": user
        }

        return render(request, 'display_profile.html', data)

def edit_profile(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    if request.user != user:
        return HttpResponseForbidden()

    form = UserEntityForm(request.POST, instance=user)

    if form.is_valid():
        user.save()
            return redirect('display_profile', request.user_id)

