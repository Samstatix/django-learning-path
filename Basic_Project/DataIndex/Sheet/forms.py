from django import forms
from .models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['Name', 'Serial', 'Birth_Date', 'Email', 'Phone', 'Address']
        widgets = {
            'Birth_Date': forms.DateInput(attrs={'type': 'date'})
        }