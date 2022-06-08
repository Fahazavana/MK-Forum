from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import FormResetPassword, FormUpdatePassword
from . import views


app_name = "user_app"

urlpatterns = [
    path("create/", views.registerUser, name='create'),
    path("login/", views.LoginUserView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='user_app:login'), name="logout"),
    path("reset-password/", views.ResetPasswordView.as_view(), name='reset_password'),
    path("reset-password/done/", PasswordResetDoneView.as_view(template_name='users/user_reset_password_done.html'),
         name='password_reset_done'),
    path("reset_password_confirm/<str:uidb64>/<str:token>/", PasswordResetConfirmView.as_view(template_name='users/user_reset_password_confirm.html',
                                                                                              form_class=FormUpdatePassword, success_url=reverse_lazy("user_app:password_reset_complete")),
         name='password_reset_confirm'),
    path("reset-password/complete/", PasswordResetDoneView.as_view(template_name='users/user_reset_password_complete.html'),
         name='password_reset_complete'),
    path("activate/<str:uidb64>/<str:token>/", views.activate,
         name='activate'),

]
