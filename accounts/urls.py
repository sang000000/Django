from django.contrib import admin
from django.urls import path,include
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("userdelete/", views.userdelete, name="userdelete"),
    path("userupdate/", views.userupdate, name="userupdate"),
    path("password/", views.password, name="password"),
]
    