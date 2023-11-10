from django import forms
from .models import EmployeeDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm


GENDER_CHOICE=(
    ('male','MALE'),
    ('female',)
)
def emailvalidator(value):
    emaillist=User.objects.filter(email=value)
    if emaillist:
        raise forms.ValidationError("Email already exist")

class SignupForm(UserCreationForm):
    password1=forms.CharField(label="password",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="password confirmation",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    empcode=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(error_messages={'required':'please enter your first name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(error_messages={'required':'please enter your last name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(validators=[emailvalidator],error_messages={'required':'please enter your Email address'},widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(label="username/E-mail",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
class EditprofileForm(forms.ModelForm):
    empcode=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    empdept=forms.CharField(label="Employee Department",widget=forms.TextInput(attrs={'class':'form-control'}))
    designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    joiningdate=forms.CharField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    class Meta:
        model=EmployeeDetail
        fields="__all__"
        exclude=['user']    
        
class EditUserForm(forms.ModelForm):
    password=None
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(error_messages={'required':'please enter your Email address'},widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(error_messages={'required':'please enter your first name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(error_messages={'required':'please enter your last name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        
        
class ChangepassForm(PasswordChangeForm):
    old_password=forms.CharField(label="current password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label="new password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="new password confirm",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
