from django import forms
from waterapp.models import emp

class empForm(forms.ModelForm):
    class Meta:
        model = emp
        fields = '__all__'