from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from .models import Profile


# After user creation, the model User send a signal (post_save)
# And received by the function below to create a User Profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
	instance.profile.save()
