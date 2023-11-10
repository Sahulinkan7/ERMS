from django.contrib import admin

# Register your models here.
from .models import EmployeeDetail

@admin.register(EmployeeDetail)
class Employeeadmin(admin.ModelAdmin):
    list_display=['id','empcode','user']
    