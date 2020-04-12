from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse

STATUS = (
    (0, "open"),
    (1, "pending"),
    (2, "closed")
)

HELP_TYPE = (
    ("WANT", "wanted"),
    ("OFFER", "offered")
)

class HelpNotice(models.Model):
    title = models.CharField(null=False, max_length=75)
    content = models.TextField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='help_notices')
    ending_at = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    updated_at = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    type = models.CharField(max_length=10, null=False, choices=HELP_TYPE)
    help_values = {'wanted': 'WANT', 'offered': 'OFFER' }

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        timestamp = timezone.now().strftime("%d-%m-%Y-%H%M%S")
        string = '{}-{}'.format(self.title, timestamp)
        return slugify(string)

    def get_absolute_url(self):
        kwargs = {'type': self.get_type_display(), 'slug': self.slug}
        return reverse('helpme:detail', kwargs=kwargs)
    
    def form_fields(self):
        return {
            'title': self.title,
            'content': self.content,
            'ending_at': self.ending_at,
            'status': self.status,
        }


@receiver(pre_save, sender=HelpNotice)
def create_title_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.get_unique_slug()

@receiver(post_save, sender=HelpNotice)
def create_user_profile(sender, instance, created, **kwargs):
    time_now = timezone.now()
    if created: instance.created_at = time_now
    instance.updated_at = time_now

