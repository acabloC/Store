from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm, forms
from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields=["username","password"]

class UserRegistrationForm(UserCreationForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholer":"D"
                                                             }))
    last_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control py-4",
        "placeholer":"d"
                                                             }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-control py-4",
        "placeholer":"Введите еmail"
                                                             }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholer": "Введите пароль"                                     }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholer": "Повторите пароль"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholer": "Введите никнейм"
    }))
