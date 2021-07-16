from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from subjects.forms import SubjectForm
from subjects.models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'


class SubjectDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'subjects.view_subject'
    model = Subject
    template_name = 'subject_detail.html'


class SubjectCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'subjects.add_subject'
    template_name = 'subject_form.html'
    model = Subject
    form_class = SubjectForm


class SubjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'subjects.delete_subject'
    model = Subject
    template_name = 'subject_confirm_delete.html'
    success_url = reverse_lazy('subjects:subject_list')


class SubjectUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'subjects.change_subject'
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_update.html'
    success_url = reverse_lazy('subjects:subject_list')

