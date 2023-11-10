from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    empcode=models.CharField(max_length=40)
    empdept=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=20,null=True)
    joiningdate=models.DateField(null=True)
    
    def __str__(self):
        return self.user.username