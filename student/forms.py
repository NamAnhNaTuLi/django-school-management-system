from django import forms
from django.forms import ModelForm

from student.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'student_lastname': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'student_firstname': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'student_gender': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'student_class': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'student_email': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'student_date_of_birth': forms.DateInput(attrs={'class': 'form-control form-control-user'}),
            'giao_vien_CN':  forms.Select(attrs={'class': 'form-control form-control-user'}),
        }
