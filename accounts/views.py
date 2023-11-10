from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,EditprofileForm,EditUserForm,ChangepassForm
from .models import EmployeeDetail
from employee.models import EmployeeEducationDetail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
# Create your views here.

def Signupview(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            firstname=fm.cleaned_data['first_name']
            lastname=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email']
            empcode=fm.cleaned_data['empcode']
            password=fm.cleaned_data['password1']
            usr=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
            EmployeeDetail.objects.create(user=usr,empcode=empcode)
            EmployeeEducationDetail.objects.create(user=usr)
            messages.success(request,"your account created successfuly !")
            return HttpResponseRedirect("/accounts/login/")
        else:
            messages.error(request,"fill the form properly")
            
    else:
        fm=SignupForm()
    return render(request,"accounts/signup.html",{'form':fm})


def loginview(request):
    if request.method=='POST':
        fm=LoginForm(request=request,data=request.POST)
        if fm.is_valid():
            usrname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            usr=authenticate(username=usrname,password=upass)
            if usr is not None:
                login(request,user=usr)
                messages.success(request,"you are logged in successfully ! ")
                return HttpResponseRedirect("/accounts/profile/")
        else:
            messages.error(request,"Invalid credentials ,please Try again !")
    else:
        fm=LoginForm()
    return render(request,"accounts/login.html",{'form':fm})

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You are logged out successfully !")
        return HttpResponseRedirect("/accounts/login/")
    else:
        return HttpResponseRedirect("/accounts/login/")
    
def profileview(request):
    if request.user.is_authenticated:
        try:
            usr=EmployeeDetail.objects.get(user=request.user)
            if request.method=='POST':
                fm=EditUserForm(request.POST,instance=request.user)
                fm2=EditprofileForm(request.POST,instance=usr)
                if fm.is_valid() and fm2.is_valid():
                    fm.save()
                    fm2.save()
                    messages.success(request,"your profile got updated !")
                else:
                    messages.error(request,"please update carefully ! ")
            else:
                fm=EditUserForm(instance=request.user)
                fm2=EditprofileForm(instance=usr)
            return render(request,"accounts/profile.html",{'form':fm,'form2':fm2})
        except:   
            messages.error(request,"Invalid User")
            return HttpResponseRedirect("/accounts/logout/")
    else:
        return HttpResponseRedirect("/accounts/login/")
    
    
def change_password_view(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=ChangepassForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Password changed successfully !")
        else:
            fm=ChangepassForm(user=request.user)
        return render(request,"accounts/changepassword.html",{'form':fm})
    else:
        return HttpResponseRedirect("/accounts/login/")
