from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.login_views, name="login"),
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_views, name="logout"),
    path("find", views.find),
]