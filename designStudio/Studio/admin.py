from django.contrib import admin
from .models import Application,Category
# Register your models here.

admin.site.register(Category)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')