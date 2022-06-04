from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.forms import AuthenticationForm


class ParagraphError(ErrorList):
    def __str__(self):
        return self.as_div()

    def as_div(self):
        if not self:
            return ''
        else:
            return '%s' % ''.join(["%s" % error for error in self])


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.error_css_class = "text-danger"
        super().__init__(*args, **kwargs)
        self.error_class = ParagraphError
        #self.error_messages['invalid_login'] = "Nom d'utilisateur ou mots de passe invalide"
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-5 my_login', "placeholder": "Nom d'utilisateur"})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-5 my_login', "placeholder": "Mot de passe"})
