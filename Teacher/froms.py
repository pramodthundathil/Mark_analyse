from django.forms import ModelForm,Textarea
from .models import *

class BookAddForm(ModelForm):
    class Meta:
        model = Books
        fields = ["bookname","auther","strem","descrioption","referencelink","book_image"]
        
class SuggestionForm(ModelForm):
    class Meta:
        model = Recomendations
        fields = ["recommendation","book"]
        
        widgets = {
            "recommendation":Textarea(attrs={"cols":"100","rows":'10',"color":"blue"})
        }