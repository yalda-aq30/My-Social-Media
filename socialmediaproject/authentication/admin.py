from django.contrib import admin
from .models import authentication

# Register your models here.

class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('nameuser' , 'password' , 'email') 