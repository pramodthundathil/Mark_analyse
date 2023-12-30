from django.forms import ModelForm 
from .models import Question 

class QuestinForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
