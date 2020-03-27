from django.contrib import admin
from .models import User

class PostAdmin(admin.ModelAdmin):

admin.site.register(User, UserAdmin)