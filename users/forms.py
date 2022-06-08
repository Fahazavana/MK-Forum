from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm, PasswordResetForm
from django.core.exceptions import ValidationError



class TextErrorList(ErrorList):
    def __str__(self):
        return self.as_div()

    def as_div(self):
        if not self:
            return ''
        else:
            return '%s' % ''.join(['%s' % e for e in self])


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_css_class = "text-danger"
        self.error_class = TextErrorList
        self.error_messages['invalid_login'] = "Saisissez un nom d’utilisateur et un mot de passe valides."
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-2 my_login', "placeholder": "Nom d'utilisateur"})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-2 my_login', "placeholder": "Mot de passe"})


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = TextErrorList
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Nom d'utilisateur"})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Votre@Email.com"})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Mot de passe"})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Re-saisir votre mots de passe"})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', "Cette addresse est déja utilisé par un autre utilisateur")
            raise ValidationError(
                f"l'email : {email} existe déja. veuiller spécifier un autre.")
        return self.cleaned_data





class FormResetPassword(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = TextErrorList
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Entrez votre e-mail"})


class FormUpdatePassword(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = TextErrorList
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Mot de passe"})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control mb-2 my_login', "placeholder": "Re-saisir votre mots de passe"})
