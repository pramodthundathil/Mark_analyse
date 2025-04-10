from django.urls import path  
from .import views  
urlpatterns = [
    path("StudentDeatilsView/<int:pk>",views.StudentDeatilsView,name="StudentDeatilsView"),
    path("StudentDeatilsViewParent/<int:pk>",views.StudentDeatilsViewParent,name="StudentDeatilsViewParent"),
    path("GiveSuggestions/<int:pk>",views.GiveSuggestions,name="GiveSuggestions"),
    path("Addbook",views.Addbook,name="Addbook"),
    path("DeleteBook/<int:pk>",views.DeleteBook,name="DeleteBook"),
    path("RecommendationsStudentView",views.RecommendationsStudentView,name="RecommendationsStudentView"),
    path("LeaveRepaly/<int:pk>",views.LeaveRepaly,name="LeaveRepaly"),
    path("DeleteRecommentation/<int:pk>",views.DeleteRecommentation,name="DeleteRecommentation"),
    path("ChatAdd",views.ChatAdd,name="ChatAdd"),

    path("add_exam",views.add_exam,name="add_exam"),
    path("add_marks_to_students",views.add_marks_to_students,name="add_marks_to_students"),
    path("add_marks/<str:student_id>",views.add_marks,name="add_marks"),
    path("view_marks_parent",views.view_marks_parent,name="view_marks_parent"),
    path("Mymarks",views.Mymarks,name="Mymarks"),
   
]
