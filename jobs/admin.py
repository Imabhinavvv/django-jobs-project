from django.contrib import admin
from .models import Job
# Register your models here.
class Jobadmin(admin.ModelAdmin):
    list_display=['company', 'role','qualification', 'salary']
admin.site.register(Job, Jobadmin)