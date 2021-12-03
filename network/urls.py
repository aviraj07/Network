
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:name>", views.profile, name="profile"),
    path("follow/<str:name>", views.follow, name="follow"),
    path("unfollow/<str:name>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("like/<int:id>", views.like, name="like"),
    path("unlike/<int:id>", views.unlike, name="unlike")

]
