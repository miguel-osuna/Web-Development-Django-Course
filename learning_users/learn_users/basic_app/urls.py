from django.urls import path
from basic_app import views

# Declare app name for template extending
app_name = "basic_app"

urlpatterns = [
    path("user_login/", views.user_login, name="user_login"),
    path("register/", views.register, name="register")
]
