from django.urls import path  
from .import views  
urlpatterns = [
    path("StudentDeatilsView/<int:pk>",views.StudentDeatilsView,name="StudentDeatilsView"),
    path("GiveSuggestions/<int:pk>",views.GiveSuggestions,name="GiveSuggestions"),
    path("Addbook",views.Addbook,name="Addbook"),
    path("DeleteBook/<int:pk>",views.DeleteBook,name="DeleteBook"),
    path("RecommendationsStudentView",views.RecommendationsStudentView,name="RecommendationsStudentView"),
    path("LeaveRepaly/<int:pk>",views.LeaveRepaly,name="LeaveRepaly"),
    path("DeleteRecommentation/<int:pk>",views.DeleteRecommentation,name="DeleteRecommentation")
]
