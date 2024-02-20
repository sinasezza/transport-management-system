from django.contrib import admin
from . import models


@admin.register(models.Account)
class AccountManager(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'first_name', 'last_name',)