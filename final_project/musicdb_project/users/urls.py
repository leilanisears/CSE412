from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    #path("profile", views.profile_page, name="profile page"),
    #path("login/", views.login, name="login"),
    #path("<user_id>/logout", views.logout, name="logout"),
    #path("register/", views.register_request, name="register"),
    path("edit/<str:user_id>/", views.edit_profile, name="edit profile"),
    path("delete/<str:user_id>", views.delete_profile, name="delete profile"),
    path("<str:user_id>/<str:action>/", views.follow_unfollow, name="follow or unfollow"),
]
