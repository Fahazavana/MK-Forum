from .forms import UserLoginForm, UserRegistrationForm, FormResetPassword
from .models import Profile
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls.base import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import DetailView
# Create your views here.


class LoginUserView(LoginView):
    """
        Login view for user
    """
    template_name = 'users/user_login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True


def registerUser(request):
    """
        Register View for new user 
    """
    if request.user.is_authenticated:
        """
            Redirect the user to the home page
            if user has already an account 
        """
        return redirect("forum_app:index")
    if request.method == 'POST':
        """
            Check registration form,
            and Send an email witha a link to activate the account
        """
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            current_domain = get_current_site(request)
            mail_subject = " Acivation Compte Mk-Forum"
            context = {
                'user': new_user,
                'domain': current_domain,
                'uid':  urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user)
            }
            print("send token", context['token'])
            messages.success(
                request, "Inscription réussie! Vérifier votre email pour l'activation")
            email_content = render_to_string(
                'users/user_activation_account.html', context=context)
            to_email = form.cleaned_data['email']
            email = EmailMessage(mail_subject, email_content, to=[to_email])
            email.send()
            return redirect("user_app:login")
    else:
        form = UserRegistrationForm()
    return render(request, 'users/user_register.html', {'form': form})


def activate(request, uidb64, token):
    """
        A view to handle the url activation.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    print("Receivd token", token)
    if (user is not None) and (account_activation_token.check_token(user, token)):
        user.is_active = True
        user.save()
        messages.success(request, "Compte activer avec succes!")
    else:
        messages.warning(request, "Lien invalide")

    return redirect('user_app:login')


class ResetPasswordView(PasswordResetView):
    """
        Password reset view
    """
    email_template_name = "users/user_reset_password_email.html"
    template_name = "users/user_reset_password.html"
    form_class = FormResetPassword
    success_url = reverse_lazy("user_app:password_reset_done")


class ProfileView(DetailView):
    template_name = "users/user_profile.html"
    model = Profile
    context_object_name = 'user_profile'

    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    # context[""] =
    # return context
