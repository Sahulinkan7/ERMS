from django import forms 

from .models import EmployeeEducationDetail,EmployeeExperience

class EmployeeEducationForm(forms.ModelForm):
    coursepg=forms.CharField(label="Post Graduate Course Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    yearofpassingpg=forms.CharField(label="Year of passing PG",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    institutepg=forms.CharField(label="Institute name of PG",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    percentagepg=forms.CharField(label="Percentage of marks in PG",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    coursegrad=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    yearofpassinggrad=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    institutegrad=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    percentagegrad=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    coursessc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    yearofpassingssc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    institutessc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    percentagessc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    coursehsc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    yearofpassinghsc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    institutehsc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    percentagehsc=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=EmployeeEducationDetail
        fields="__all__"
        exclude=['user']
        
class ExperienceForm(forms.ModelForm):
    company1name=forms.CharField(required=False,label="First company Name",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company1designation=forms.CharField(required=False,label="First company Designation",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company1salary=forms.DecimalField(required=False,label="First company Salary",widget=forms.NumberInput(attrs={'class':'form-control'}))
    company1duration=forms.DecimalField(required=False,label="First company duration",widget=forms.TextInput(attrs={'class':'form-control'}))
    company2name=forms.CharField(required=False,label="Second company Name",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company2designation=forms.CharField(required=False,label="Second company Designation",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company2salary=forms.DecimalField(required=False,label="Second company Salary",widget=forms.TextInput(attrs={'class':'form-control'}))
    company2duration=forms.DecimalField(required=False,label="Second company duration",widget=forms.TextInput(attrs={'class':'form-control'}))
    company3name=forms.CharField(required=False,label="Third company Name",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company3designation=forms.CharField(required=False,label="Third company Designation",max_length=35,widget=forms.TextInput(attrs={'class':'form-control'}))
    company3salary=forms.DecimalField(required=False,label="Third company Salary",widget=forms.TextInput(attrs={'class':'form-control'}))
    company3duration=forms.DecimalField(required=False,label="Third company duration",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=EmployeeExperience
        fields="__all__"
        exclude=['user']