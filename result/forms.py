import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _

from result.models import SubjectScore


def convert(x):
    return [float(i) for i in x.split()]


def clean_diem(data):
    if any([bool(re.findall(r"^\d+\.\d+$|^\d+$", i)) == False for i in data.split()]):
        raise ValidationError(_('chi duoc nhap ky tu so'))
    if any([i > 10 or i < 0 for i in convert(data)]):
        raise ValidationError(_('diem so khong hop le'))


class SubjectScoreForm(forms.ModelForm):

    def clean_diem_he_so_1(self):
        data = self.cleaned_data['diem_he_so_1']
        clean_diem(data)
        return data

    def clean_diem_he_so_2(self):
        data = self.cleaned_data['diem_he_so_2']
        clean_diem(data)
        return data

    def clean_diem_he_so_3(self):
        data = self.cleaned_data['diem_he_so_3']
        clean_diem(data)
        return data

    class Meta:
        model = SubjectScore
        fields = '__all__'
        widgets = {
            'student': forms.HiddenInput(),
            'subject': forms.Select(attrs={'class': 'form-control form-control-user'}),
            'diem_he_so_1': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'diem_he_so_2': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'diem_he_so_3': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                # 'unique_together': "%(model_name)s's %(field_labels)s are not unique.11111",
                'unique_together': "Diem mon hoc da ton tai",
            }
        }
        help_texts = {
            'diem_he_so_1': 'Nhap cac diem ngan cach bang dau khoang trang [\' \']'
        }


class SubjectScoreUpdateForm(forms.ModelForm):

    def clean_diem_he_so_1(self):
        data = self.cleaned_data['diem_he_so_1']
        clean_diem(data)
        return data

    def clean_diem_he_so_2(self):
        data = self.cleaned_data['diem_he_so_2']
        clean_diem(data)
        return data

    def clean_diem_he_so_3(self):
        data = self.cleaned_data['diem_he_so_3']
        clean_diem(data)
        return data

    class Meta:
        model = SubjectScore
        fields = '__all__'
        widgets = {
            'student': forms.HiddenInput(),
            'subject': forms.HiddenInput(),
            'diem_he_so_1': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'diem_he_so_2': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'diem_he_so_3': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                # 'unique_together': "%(model_name)s's %(field_labels)s are not unique.11111",
                'unique_together': "Diem mon hoc da ton tai",
            }
        }
        help_texts = {
            'diem_he_so_1': 'Nhap cac diem ngan cach bang dau khoang trang [\' \']'
        }

