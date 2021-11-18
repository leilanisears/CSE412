from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    #path("profile", views.profile_page, name="profile page"),
    path("register", views.register_request, name="register"),
]
