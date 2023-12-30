from django.urls import path  
from .import views

urlpatterns = [
    path("MarkInput",views.MarkInput,name="MarkInput"),
    path("AddQuestion",views.AddQuestion,name="AddQuestion"),
    path("Aptitudetest",views.Aptitudetest,name="Aptitudetest"),
    path("MarkProfile",views.MarkProfile,name="MarkProfile"),
    path("PredictScore",views.PredictScore,name="PredictScore"),
    path("DeleteQuestion/<int:pk>",views.DeleteQuestion,name="DeleteQuestion")
]
  

