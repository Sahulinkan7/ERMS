from django.urls import path
from. import views 

urlpatterns = [
    path("signup/",views.Signupview,name="signup"),
    path("login/",views.loginview,name="login"),
    path("logout/",views.logoutview,name="logout"),
    path("profile/",views.profileview,name="profile"),
    path("changepass/",views.change_password_view,name="changepass")
]
