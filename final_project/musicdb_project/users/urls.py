from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    #path("profile", views.profile_page, name="profile page"),
    #path("login/", views.login, name="login"),
    #path("<user_id>/logout", views.logout, name="logout"),
    #path("register/", views.register_request, name="register"),
    path("edit/", views.edit_profile, name="edit profile"),
    path("delete/", views.delete_profile, name="delete profile"),
    path("<user_id>/follow_unfollow", views.follow_unfollow, name="follow or unfollow"),
]
