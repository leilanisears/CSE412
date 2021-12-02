from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserUpdateForm
from .models import User
#from musicdb.views import welcome

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful. You are now being redirected to home page!')
#             return redirect('home')
#         messages.error(request, 'Registration was unsuccessful. Invalid information provided.')
#     else:
#         form = RegistrationForm()
#     return render(request,'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Profile Updated Successfully.')
            return redirect()
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'user.html', context)

@login_required
def follow_unfollow(request, username):
    user = get_object_or_404(User, id=username)

    other_user_id = request.data.get('username')
    other_user = get_object_or_404(User, id=other_user_id)

    req_type = request.data.get('type')

    if req_type == "follow":
        user.following.add(other_user)
        other_user.followers.add(user)

        success_message = "You are now following " + other_user.username
        messages.success(request, success_message)

        return redirect("display_profile")

    if req_type == "unfollow":
        user.following.remove(other_user)
        other_user.followers.remove(user)

        success_message = "You are no longer following " + other_user.display_name
        messages.success(request, success_message)

        return redirect("display_profile")

    messages.error(request, "Unexpected error. Please try again later")
    return redirect('display_profile', request)

def error_request(request):
    context = {}

    return render(request, "error_request.html", context)

@login_required
def delete_profile(request, username):
    user = get_object_or_404(User, id=username)

    if request.user != user:
        return HttpResponseForbidden()

    user.remove()
    return redirect('musicdb:home', request)

# def display_profile(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)

#     if request.user != user:
#         return HttpResponseForbidden()

#     if request.method == "GET":
#         data = {
#             "user": user
#         }

#         return render(request, 'display_profile.html', data)

# def edit_profile(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)

#     if request.user != user:
#         return HttpResponseForbidden()

#     form = UserEntityForm(request.POST, instance=user)

#     if form.is_valid():
#         user.save()
#         return redirect('display_profile', request.user_id)

#     messages.error(request, "There was an error while editing your profile.")
#     return redirect('display_profile', request)
