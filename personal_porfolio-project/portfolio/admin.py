from django.contrib import admin

from .models import Project

#displays this model inside the admin url
admin.site.register(Project)