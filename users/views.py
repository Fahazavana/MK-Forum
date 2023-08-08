from .forms import UserLoginForm, UserRegistrationForm, FormResetPassword, UpdateUserForm, UpdateUserProfileForm, FormChangePassword, UpdateUserProfilePictureForm
from .models import Profile
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls.base import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import DetailView, DeleteView, UpdateView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
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
            if user loged in
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

# Acount activation


def activate(request, uidb64, token):
    """
        A view to handle the url activation.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
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


class NewPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
        Change password
    """
    template_name = 'users/user_password_change.html'
    form_class = FormChangePassword

    def form_valid(self, form):
        if not form.is_valid():
            print('form is not valid')
            raise ValueError('Form is not valid')
        response = super().form_valid(form)
        messages.success(
            self.request, 'Votre mot de passe a été changé avec succès.')
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy('user_app:profile', kwargs={'pk': self.kwargs['pk']})


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "users/user_profile.html"
    model = Profile
    context_object_name = 'user_profile'



class UserAccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User  # Replace with your user model
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("forum_app:index")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Compte avec succes")
        logout(request)

        return super().delete(request, *args, **kwargs)


@login_required
def updateUserProfile(request, pk):
    if request.method == 'POST':
        userForm = UpdateUserForm(request.POST, instance=request.user)
        profileForm = UpdateUserProfileForm(
            request.POST, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            user_form = userForm.save()
            profile = profileForm.save(False)
            profile.user = user_form
            profile.save()
            messages.success(request, "Information mis a jour avec succes")
            return redirect('user_app:profile', pk)
    else:
        username = User.objects.get(pk=pk).username
        userForm = UpdateUserForm(instance=request.user)
        profileForm = UpdateUserProfileForm(instance=request.user.profile)
        context = {'userForm': userForm, 'profileForm': profileForm,
                   'username': username}
        return render(request, 'users/user_edit.html', context)


class UserChangeProfilePicture(LoginRequiredMixin, UpdateView):
    template_name = "users/user_picture.html"
    model = Profile
    form_class = UpdateUserProfilePictureForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        # Get the old pic
        # check if it exisit then delete
        old_pic = user.profile.profile_pic.path
        if os.path.exists(old_pic):
            user.profile.profile_pic.delete()

        # Get the new pic
        # rename it and adjust the path
        pic = form.cleaned_data['profile_pic']
        print("PIIIIC",pic)
        new_pic_name = f"{user.id}_{user.username}.{str(pic).split('.')[-1]}"
        new_pic_path = os.path.join('static/media', new_pic_name)
        # Write the file with the new filename
        with open(new_pic_path, 'wb+') as destination:
            for chunk in pic.chunks():
                destination.write(chunk)

        user.profile.profile_pic = new_pic_name  # Update the profile picture field
        user.profile.save()  # Save the profile model to persist the changes
        return response