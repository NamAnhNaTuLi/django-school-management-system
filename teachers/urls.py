from django.urls import path, re_path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.TeacherListView.as_view(), name='teacher-list'),
    path('<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('create/', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('update/<int:pk>', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('delete/<int:pk>', views.TeacherDeleteView.as_view(), name='teacher-delete'),
]