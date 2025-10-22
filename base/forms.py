from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'disease', 'doctor_assigned', 'age', 'room_number']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'disease': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter disease'
            }),
            'doctor_assigned': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter doctor name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'room_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room number'
            }),
        }
