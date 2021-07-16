from django import forms
from django.forms import ModelForm

from subjects.models import Subject, Khoa


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'subject_unit': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
        }


class DepartmentForm(ModelForm):
    class Meta:
        model = Khoa
        fields = '__all__'
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }