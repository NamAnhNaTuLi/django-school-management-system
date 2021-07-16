from django.urls import path

from student.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView
from result.views import SubjectScoreCreat

app_name = 'students'

urlpatterns = [
    path('list/', StudentListView.as_view(), name='student_list'),
    path('<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete'),

    path('<int:pk>/addscore/', SubjectScoreCreat.as_view(), name='subject-score-create'),
]