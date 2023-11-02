from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(AdvUser)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')