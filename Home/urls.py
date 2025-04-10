from django.urls import path  
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("Parent_signup",views.Parent_signup,name="Parent_signup"),
    path("ParentHome",views.ParentHome,name="ParentHome"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("TeacherHome",views.TeacherHome,name="TeacherHome"),
    path("AddTeacher",views.AddTeacher,name="AddTeacher"),
    path("TeacherDelete/<int:pk>",views.TeacherDelete,name="TeacherDelete"),
    
]
