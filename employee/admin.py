from django.contrib import admin
from .models import EmployeeEducationDetail,EmployeeExperience
# Register your models here.

@admin.register(EmployeeEducationDetail)
class EducationAdmin(admin.ModelAdmin):
    list_display=['id','user']



@admin.register(EmployeeExperience)
class EducationAdmin(admin.ModelAdmin):
    list_display=['id','user']
