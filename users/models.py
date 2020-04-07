# users/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return (self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to='avatar/')
    location = models.CharField(max_length=20, choices=settings.REGISTERED_COMMUNITIES)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.user.slug})

    def form_dict(self):
        return {'bio': self.bio, 'avatar': self.avatar, 'location': self.location}

@receiver(pre_save, sender=User)
def create_username_slug(sender, instance, *args, **kwargs):
    if not instance.slug: 
        instance.slug = slugify(instance.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()