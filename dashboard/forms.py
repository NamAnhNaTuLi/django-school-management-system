from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.contrib.auth.models import User
import re


class NewUserForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nhap email'}))
    last_name = forms.CharField(label="Ho", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nhap ho'}))
    first_name = forms.CharField(label="Ten", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nhap ten'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['placeholder'] = 'Nhap ten nguoi dung'
        self.fields['username'].label = 'Ten nguoi dung'
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password1'].widget.attrs['placeholder'] = 'Nhap mat khau'
        self.fields['password1'].label = 'Nhap mat khau'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password2'].widget.attrs['placeholder'] = 'Xac nhan mat khau'
        self.fields['password2'].label = 'Nhap lai mat khau'
        self.fields['password2'].help_text = ''

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong trung khop")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email da duoc dang ky. Vui long chon email khac')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'type':'email'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
    first_name = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ''
        self.fields['password'].help_text= "<a href=\"../changepassword/\">Thay doi mat khau</a>"


class PasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Mat khau cu'
        self.fields['old_password'].label = 'Nhap mat khau cu'

        self.fields['new_password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Mat khau moi'
        self.fields['new_password1'].label = 'Nhap mat khau moi'
        self.fields['new_password1'].help_text=['Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn', 'Mật khẩu của bạn phải chứa ít nhất 8 ký tự', 'Mật khẩu của bạn không thể là mật khẩu thường dùng', 'Mật khẩu của bạn không được hoàn toàn là số']

        self.fields['new_password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Xac nhan mat khau'
        self.fields['new_password2'].label = 'Nhap mat lai khau'

        self.error_messages['password_incorrect'] = "Mật khẩu cũ của bạn đã được nhập không chính xác. Vui lòng nhập " \
                                                    "lại. "
        self.error_messages['password_mismatch'] = 'Hai trường mật khẩu không khớp.'


class ResetPasswordForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control form-control-user', 'placeholder':'Nhap email'})
    )


class SetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Mat khau moi'
        self.fields['new_password1'].label = 'Nhap mat khau moi'
        self.fields['new_password1'].help_text=['Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn', 'Mật khẩu của bạn phải chứa ít nhất 8 ký tự', 'Mật khẩu của bạn không thể là mật khẩu thường dùng', 'Mật khẩu của bạn không được hoàn toàn là số']

        self.fields['new_password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Xac nhan mat khau'
        self.fields['new_password2'].label = 'Nhap mat lai khau'

        self.error_messages['password_mismatch'] = 'Hai trường mật khẩu không khớp.'
