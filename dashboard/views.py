from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import re
# Create your views here.
from django.views.generic import TemplateView

from classes.models import Class
from dashboard.forms import NewUserForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from student.models import Student
from teachers.models import Teacher
from subjects.models import Subject


class HomePageView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_student'] = Student.objects.all().count()
        context['num_teacher'] = Teacher.objects.all().count()
        context['num_class'] = Class.objects.all().count()
        return context


def loginrequest(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Ten tai khoang va mat khau khong hop le')
    return render(request, 'registration/login.html')


def registeruser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password1']
            user_obj = authenticate(request, username=user_name, password = pass_word)
            login(request, user_obj)
            messages.success(request, "Dang ky tai khoan thanh cong", extra_tags='green')
            # return redirect('login')
        else:
            messages.error(request, 'Dang ky tai khoan khong thanh cong')
    else:
        form = NewUserForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)


def editprofile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Cap nhat thong tin tai khoan thanh cong"))
        else:
            messages.error(request, 'Cap nhat thong tin khong thanh cong')
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'registration/editprofile.html', context)


# def changepassword(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Thay doi mat khau thanh cong", extra_tags='green')
#         else:
#             messages.error(request, 'Thay doi mat khau khong thanh cong')
#     else:
#         form = PasswordChangeForm(user=request.user)
#     context = {'form': form}
#     return render(request, 'registration/changepassword.html', context)


# def resetpassword(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Da gui mail')
#         else:
#             messages.error(request, 'Gui mail xac thuc khong thanh cong')
#     else:
#         form = PasswordResetForm()
#     context = {'form': form}
#     return render(request, 'registration/resetpassword.html', context)

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    gender_male = Student.objects.filter(student_gender="Nam").count()
    gender_female = Student.objects.filter(student_gender="Nu").count()
    gender_other = Student.objects.filter(student_gender="Khac").count()
    gender_list = [gender_male, gender_female, gender_other]

    student_all = Student.objects.all()
    class_all = Class.objects.all()

    grade_list = sorted({re.split('[a-zA-Z]', one_class.class_name, 1)[0] for one_class in class_all})
    grade_name_list = ['Khoi ' + grade for grade in grade_list]
    student_in_grade_count_list = []
    for grade in grade_list:
        students = Student.objects.filter(student_class__class_name__istartswith=grade).count()
        student_in_grade_count_list.append(students)

    panel_list = sorted({re.findall('[a-zA-Z]', one_class.class_name)[0] for one_class in class_all})
    panel_list_name = ['Ban ' + panel for panel in panel_list]
    student_in_panel_count_list = []
    for panel in panel_list:
        students = Student.objects.filter(student_class__class_name__contains=panel).count()
        student_in_panel_count_list.append(students)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_student'] = Student.objects.all().count()
        context['num_teacher'] = Teacher.objects.all().count()
        context['num_class'] = Class.objects.all().count()
        context['num_subject'] = Subject.objects.all().count()
        context['gender_list'] = self.gender_list

        context['grade_name_list'] = self.grade_name_list
        context['student_in_grade_count_list'] = self.student_in_grade_count_list

        context['panel_list_name'] = self.panel_list_name
        context['student_in_panel_count_list'] = self.student_in_panel_count_list
        return context