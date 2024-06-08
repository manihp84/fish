from django import forms
from .models import emp, signup, login

class empForm(forms.ModelForm):
    class Meta:
        model = emp
        fields = '__all__'

class signupmodel(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'

class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'