from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm, PasswordResetForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import Profile


class TextErrorList(ErrorList):
    def __str__(self):
        return self.as_div()

    def as_div(self):
        if not self:
            return ''
        else:
            return '%s' % ''.join(['<div class="text-danger">%s</div>' % e for e in self])


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
        self.error_css_class = "text-danger"
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
        self.error_css_class = "text-danger"
        self.error_class = TextErrorList
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Entrez votre e-mail"})


class FormUpdatePassword(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_css_class = "text-danger"
        self.error_class = TextErrorList
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Mot de passe"})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control mb-2 my_login', "placeholder": "Re-saisir votre mots de passe"})




class FormChangePassword(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_css_class = "text-danger"
        self.error_class = TextErrorList
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "ancien mots de passe"})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', "placeholder": "Mot de passe"})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control mb-2 my_login', "placeholder": "Re-saisir votre mots de passe"})



# Updating User


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', 'placeholder': 'Prenom(s)'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', 'placeholder': 'Nom'})

# Update Profile


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dateNaissance', 'niveaux', 'adresse']
        widgets = {'dateNaissance': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateNaissance'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login'})
        self.fields['niveaux'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', 'placeholder': 'Niveaux'})
        self.fields['adresse'].widget.attrs.update(
            {'class': 'form-control mb-3 my_login', 'placeholder': 'Adresse'})
        
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            if instance.dateNaissance !=None:
                self.initial['dateNaissance'] = self.instance.dateNaissance.isoformat()
                
                
class UpdateUserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs.update(
            {'class': 'form-control mt-2 mb-3'})

