from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from result.forms import SubjectScoreForm, SubjectScoreUpdateForm
from result.models import SubjectScore
from student.models import Student


class SubjectScoreCreat(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'result.add_subjectscore'
    model = SubjectScore
    form_class = SubjectScoreForm
    template_name = 'subjectscore_form.html'

    # success_url = reverse_lazy('student-list')
    # fields = '__all__'

    def get_initial(self):
        initial = super().get_initial()
        if self.request.method not in ('POST', 'PUT'):
            student = get_object_or_404(Student, id=self.kwargs['pk'])
            initial['student'] = student
        return initial

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:student-detail', args=(self.object.student.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = get_object_or_404(Student, id=self.kwargs['pk'])
        context['student_name'] = student
        return context

    def form_valid(self, form):
        return super(SubjectScoreCreat, self).form_valid(form)


class SubjectScoreUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'result.change_subjectscore'
    model = SubjectScore
    form_class = SubjectScoreUpdateForm
    template_name = 'subjectscore_update.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:student-detail', args=(self.object.student.id,))


class SubjectScoreDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'result.delete_subjectscore'
    model = SubjectScore
    template_name = 'subjectscore_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:student-detail', args=(self.object.student.id,))

