from django.contrib import admin

# Register your models here.

from .models import Categories, Job

admin.site.register(Job)
admin.site.register(Categories)