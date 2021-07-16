from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from classes.forms import ClassForm, StudentForm
from classes.models import Class
from student.models import Student


class ClassListView(ListView):
    model = Class
    template_name = 'class_list.html'


class ClassDetailView(LoginRequiredMixin, DetailView):
    model = Class
    template_name = 'class_detail.html'
    slug_field = 'class_name'
    slug_url_kwarg = 'class_name'


class ClassCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'classes.add_class'
    template_name = 'class_form.html'
    model = Class
    form_class = ClassForm


class ClassDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'classes.delete_class'
    model = Class
    template_name = 'class_confirm_delete.html'
    success_url = reverse_lazy('classes:class-list')
    slug_field = 'class_name'
    slug_url_kwarg = 'class_name'


class ClassUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'classes.change_class'
    model = Class
    form_class = ClassForm
    template_name = 'class_update.html'
    slug_field = 'class_name'
    slug_url_kwarg = 'class_name'
    success_url = reverse_lazy('classes:class-list')


class ClassDetailStudentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'student.add_student'
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'

    def form_valid(self, form):
        student_class = get_object_or_404(Class, class_name=self.kwargs['class_name'])
        form.instance.student_class = student_class
        return super(ClassDetailStudentCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('classes:class-detail', args=(self.object.student_class,))


class ClassDetailStudentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'student.change_student'
    model = Student
    form_class = StudentForm
    template_name = 'student_update.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('classes:class-detail', args=(self.object.student_class,))


class ClassDetailStudentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'student.delete_student'
    model = Student
    template_name = 'student_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('classes:class-detail', args=(self.object.student_class,))

