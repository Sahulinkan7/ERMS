from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeEducationForm,ExperienceForm
from .models import EmployeeEducationDetail,EmployeeExperience
from django.contrib import messages
# Create your views here.


def show_education(request):
    if request.user.is_authenticated:
        employee=EmployeeEducationDetail.objects.get(user=request.user)
        return render(request,"employee/show_education.html",{'employee':employee})
    else:
        return HttpResponseRedirect("/accounts/login/")


def edit_employee_education_view(request):
    if request.user.is_authenticated:
        user=EmployeeEducationDetail.objects.get(user=request.user)
        if request.method=='POST':
            fm=EmployeeEducationForm(request.POST,instance=user)
            if fm.is_valid():
                fm.save()
                messages.success(request,f"Education details updated successfully !")
            else:
                messages.error(request,f"please check some errors present ")
        else:
            fm=EmployeeEducationForm(instance=user)
        return render(request,"employee/emp_education.html",{'form':fm})
    else:
        return HttpResponseRedirect("/accounts/login/")
    
    
def edit_employee_experience_view(request):
    if request.user.is_authenticated:
        user=EmployeeExperience.objects.get(user=request.user)
        if request.method=='POST':
            fm=ExperienceForm(request.POST,instance=user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Experience updated successfully ")
        else:
            fm=ExperienceForm(instance=user)
        return render(request,"employee/edit_experience.html",{'form':fm})
    else:
        return HttpResponseRedirect("/accounts/login/")