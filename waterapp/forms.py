from django import forms
from .models import emp, signup

class empForm(forms.ModelForm):
    class Meta:
        model = emp
        fields = '__all__'

class signupmodel(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'