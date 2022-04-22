from django.contrib import admin
from .models import Blog

#displays this model inside the admin url
admin.site.register(Blog)
