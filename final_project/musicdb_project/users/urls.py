from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    #path("profile", views.profile_page, name="profile page"),
    path("register", views.register_request, name="register"),
    path("edit", views.edit_profile, name="edit profile"),
    path("delete", views.delete_profile, name="delete profile"),
]
