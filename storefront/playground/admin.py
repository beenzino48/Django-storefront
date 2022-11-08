from django.contrib import admin
from . import models

# admin user is created
# the way lists are displayed is decided
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')

admin.site.register(models.Post, AuthorAdmin)
