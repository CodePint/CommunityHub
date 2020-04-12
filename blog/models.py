from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.urls import reverse
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from datetime import datetime, timedelta


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(max_length=25000)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        timestamp = timezone.now().strftime("%d-%m-%Y-%H%M%S")
        string = '{}-{}'.format(self.title, timestamp)
        return slugify(string)

    def get_absolute_url(self):
        kwargs = {'author': self.author.slug, 'slug': self.slug}
        return reverse('blog:detail', kwargs=kwargs)

@receiver(pre_save, sender=Post)
def create_title_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.get_unique_slug()


@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    time_now = timezone.now()
    if created: instance.created_at = time_now
    instance.updated_at = time_now
