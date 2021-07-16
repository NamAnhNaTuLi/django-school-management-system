from django.urls import path

from subjects.views import SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('<int:pk>', SubjectDetailView.as_view(), name='subject-detail'),
    path('create/', SubjectCreateView.as_view(), name='subject_create'),
    path('update/<int:pk>', SubjectUpdateView.as_view(), name='subject_update'),
    path('delete/<int:pk>', SubjectDeleteView.as_view(), name='subject_delete'),
]