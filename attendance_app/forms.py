from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'})
        }
