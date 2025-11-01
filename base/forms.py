from django import forms
from .models import Patient, Disease

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'disease', 'doctor_assigned', 'age', 'room_number','patient_image']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Patient name'
            }),
            'disease': forms.Select(attrs={'class': 'form-control'}),
            'doctor_assigned': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Disease name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'room_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room number'
            }),
            'patient_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),

        }

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Disease name'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Symptoms'}),
            'treatment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Treatment'})}