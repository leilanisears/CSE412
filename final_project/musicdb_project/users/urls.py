from django.urls import path
from .views import (
    profile,
    login,
    logout,
    register,
    delete_profile,
    follow_unfollow,
)
from . import views

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path('<str:user_id>/', profile, name="profile"),
    path("delete/<str:user_id>", delete_profile, name="delete-profile"),
    path("<str:user_id>/<str:action>/", follow_unfollow, name="follow-unfollow"),
]
