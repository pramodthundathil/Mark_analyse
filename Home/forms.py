from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput,PasswordInput
from django.contrib.auth.models import User

class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]
        
        widgets = {
            'username': TextInput(attrs={'placeholder':'User Name'}),
            'first_name': TextInput(attrs={'placeholder':'First Name'}),
            'last_name': TextInput(attrs={'placeholder':'Last Name'}),
            'email': TextInput(attrs={'placeholder':'Email Id'}),
            "password1": PasswordInput(attrs={'placeholder':'Email Id'})

        }