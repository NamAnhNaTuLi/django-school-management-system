from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from teachers.forms import TeacherForm
from teachers.models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'teachers.add_teacher'
    template_name = 'teacher_form.html'
    model = Teacher
    form_class = TeacherForm


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'teachers.delete_teacher'
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = reverse_lazy('teachers:teacher-list')


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'teachers.change_teacher'
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher_update.html'
    success_url = reverse_lazy('teachers:teacher-list')