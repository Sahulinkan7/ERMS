from django.urls import path 
from . import views 


urlpatterns = [
    path("education/",views.edit_employee_education_view,name="education"),
    path("showeducation/",views.show_education,name="showeducation"),
    path("experiences/",views.edit_employee_experience_view,name="experience")
]
