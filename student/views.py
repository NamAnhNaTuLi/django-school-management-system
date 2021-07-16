from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from result.models import SubjectScore
from student.forms import StudentForm
from student.models import Student
from subjects.models import Subject


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'


def phanloai(x):
    if x == '':
        return ''
    elif x >= 8:
        return "Gioi"
    elif x >= 7:
        return "Kha"
    elif x >= 6:
        return "Trung binh"
    else:
        return "Yeu"


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'student.view_student'
    model = Student
    template_name = 'student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoc_sinh = get_object_or_404(Student, id=self.kwargs['pk'])
        list_diemTB = [mon.diemTB() for mon in hoc_sinh.subjectscore_set.all()]
        if all(list_diemTB) and len(list_diemTB) > 0:
            diem_TB_tong = round(sum(list_diemTB) / len(list_diemTB), 2)
            context['diem_TB_tong'] = diem_TB_tong
            context['phan_loai_chung'] = phanloai(diem_TB_tong)
        return context


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'student.add_student'
    template_name = 'student_form.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        student = super(StudentCreateView, self).form_valid(form)
        for subject in Subject.objects.all():
            SubjectScore.objects.create(subject=subject, student=self.object)
        return student


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'student.delete_student'
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('students:student_list')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'student.change_student'
    model = Student
    form_class = StudentForm
    template_name = 'student_update.html'
    success_url = reverse_lazy('students:student_list')
