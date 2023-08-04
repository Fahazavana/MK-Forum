from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    SHCOOL_LEVEL_CHOICE = [('SEC', 'Seconde'),
                           ('PRE', 'Première'),
                           ('TER', 'Terminale'),
                           ('L1', 'Licence 1'),
                           ('L2', 'Licence 2'),
                           ('L3', 'Licence 3'),
                           ('M1', 'Master 1'),
                           ('M2', 'Master 2'),
                           ('OTH', 'Autre'),
                           ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    dateNaissance = models.DateField(
        blank=True, null=True, verbose_name='Date de naissance')
    niveaux = models.CharField(
        blank=True, max_length=4, choices=SHCOOL_LEVEL_CHOICE)
    adresse = models.CharField(blank=True, max_length=50)
    profile_pic = models.ImageField(null=True,blank=True,default=None)

    def __str__(self):
        return "{} {}".format(self.user.id, self.user.username)

    def get_absolute_url(self):
        return reverse('user_app:profile', kwargs={'pk': self.pk})
