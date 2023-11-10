from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class EmployeeEducationDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    coursepg=models.CharField(max_length=100,null=True)
    institutepg=models.CharField(max_length=200,null=True)
    yearofpassingpg=models.DateField(null=True)
    percentagepg=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    coursegrad=models.CharField(max_length=100,null=True)
    institutegrad=models.CharField(max_length=200,null=True)
    yearofpassinggrad=models.DateField(null=True)
    percentagegrad=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    coursessc=models.CharField(max_length=100,null=True)
    institutessc=models.CharField(max_length=200,null=True)
    yearofpassingssc=models.DateField(null=True)
    percentagessc=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    coursehsc=models.CharField(max_length=100,null=True)
    institutehsc=models.CharField(max_length=200,null=True)
    yearofpassinghsc=models.DateField(null=True)
    percentagehsc=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    
    def __str__(self):
        return self.user.username
    
class EmployeeExperience(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company1name=models.CharField(max_length=100,null=True)
    company1designation=models.CharField(max_length=100,null=True)
    company1salary=models.IntegerField(null=True)
    company1duration=models.DecimalField(max_digits=2,decimal_places=1,null=True)
    company2name=models.CharField(max_length=100,null=True)
    company2designation=models.CharField(max_length=100,null=True)
    company2salary=models.IntegerField(null=True)
    company2duration=models.DecimalField(max_digits=2,decimal_places=1,null=True)
    company3name=models.CharField(max_length=100,null=True)
    company3designation=models.CharField(max_length=100,null=True)
    company3salary=models.IntegerField(null=True)
    company3duration=models.DecimalField(max_digits=2,decimal_places=1,null=True)
    
    def __str__(self):
        return self.user.username