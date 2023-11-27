from django import forms
from .models import Robot,Habitacion

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class RobotForm(forms.ModelForm):
    class Meta:
        model=Robot
        fields = '__all__'
class HabitaForm(forms.ModelForm):
    class Meta:
        model=Habitacion
        fields = '__all__'
