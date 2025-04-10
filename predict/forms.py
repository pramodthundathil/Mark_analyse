from django.forms import ModelForm 
from .models import Question 
from .models import Examination, mark_exams
from django import forms

class QuestinForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class ExaminationForm(ModelForm):
    class Meta:
        model = Examination
        fields = "__all__"
        widgets = {
            'exam_name': forms.TextInput(attrs={'class': 'form-control'}),
            'exam_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class MarkExamsForm(ModelForm):
    class Meta:
        model = mark_exams
        exclude =["user","date"]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }