from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = "user_app"

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='user_app:login'), name="logout"),
    path("create/", views.registerUser, name='create')
]
