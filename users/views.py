from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import UserLoginForm, UserRegistrationForm, FormResetPassword

# Create your views here.


class LoginUserView(LoginView):
    template_name = 'users/user_login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("forum_app:index")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("user_app:login")
    else:
        form = UserRegistrationForm()
    return render(request, 'users/user_register.html', {'form': form})


class ResetPasswordView(PasswordResetView):
    email_template_name = "users/user_reset_password_email.html"
    template_name = "users/user_reset_password.html"
    form_class = FormResetPassword
    success_url = reverse_lazy("user_app:password_reset_done")
