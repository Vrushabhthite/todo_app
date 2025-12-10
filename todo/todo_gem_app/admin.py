from django.contrib import admin
from .models import Task

# Register your models here.

class taskadmin(admin.ModelAdmin):     #for dispaly list of filde
    list_display=('task','is_completed','is_created','is_updated')
    search_fields=('task',)
admin.site.register(Task,taskadmin)