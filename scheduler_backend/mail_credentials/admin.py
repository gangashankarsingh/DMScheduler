from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import RecepientContacts, Authentication

admin.site.register(RecepientContacts)
admin.site.register(Authentication)