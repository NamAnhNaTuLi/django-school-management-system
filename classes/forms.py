from django import forms
from django.forms import ModelForm

from classes.models import Class
from student.models import Student


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'giao_vien_CN':  forms.Select(attrs={'class': 'form-control form-control-user'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('student_class',)