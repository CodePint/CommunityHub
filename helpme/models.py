from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse

STATUS = (
    (0, "OPEN"),
    (1, "PENDING"),
    (2, "CLOSED")
)

HELP = (
    (0, "WANTED"),
    (1, "OFFERED")
)

class HelpNotice(models.Model):
    title = models.CharField(max_length=75)
    type = models.IntegerField(choices=HELP)
    content = models.TextField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='help_notices')
    ending_at = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    updated_at = models.DateTimeField(auto_now= True)
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
        return reverse('help:detail', kwargs={'slug': self.slug })

@receiver(pre_save, sender=HelpNotice)
def create_title_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.get_unique_slug()

