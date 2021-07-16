from django.urls import path, re_path
from result import views

app_name = 'results'

urlpatterns = [
    path('subjectscore/<int:pk>/update/', views.SubjectScoreUpdate.as_view(), name='subject-score-update'),
    path('subjectscore/<int:pk>/delete/', views.SubjectScoreDelete.as_view(), name='subject-score-delete'),
]