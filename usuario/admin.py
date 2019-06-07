from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    pass


admin.site.register(Author, AuthorAdmin)