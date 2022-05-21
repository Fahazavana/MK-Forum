from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateNaissance = models.DateField(
        blank=True, null=True, verbose_name='Date de naissance')
    profession = models.CharField(blank=True, max_length=50)
    adresse = models.CharField(blank=True, max_length=50)

# Surcharge de la methode __str__
    def __str__(self):
        return "{} {}".format(self.user.id, self.user.username)

	# Retourne l'url ver l' profile de l'utilisateur
    def get_absolute_url(self):
        return reverse('users_app:profile', kwargs={'pk': self.pk})
