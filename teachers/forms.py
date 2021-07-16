from django import forms
from django.forms import ModelForm

from teachers.models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'khoa':  forms.Select(attrs={'class': 'form-control form-control-user'}),
            'bo_mon': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }
