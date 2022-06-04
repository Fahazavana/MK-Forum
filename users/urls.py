from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, ParagraphError
from . import views


app_name = "user_app"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/user_login.html",
         authentication_form=LoginForm), name="login"),
   	path("logout/", LogoutView.as_view(next_page='user_app:login'), name="logout")]
