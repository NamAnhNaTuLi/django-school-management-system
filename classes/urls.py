from django.urls import path, re_path
from classes import views

app_name = 'classes'

urlpatterns = [
    path('list/', views.ClassListView.as_view(), name='class-list'),
    re_path(r'^(?P<class_name>[-\w]+)$', views.ClassDetailView.as_view(), name='class-detail'),
    path('create/', views.ClassCreateView.as_view(), name='class-create'),
    re_path(r'^(?P<class_name>[-\w]+)/update/$', views.ClassUpdateView.as_view(), name='class-update'),
    re_path(r'^(?P<class_name>[-\w]+)/delete/$', views.ClassDeleteView.as_view(), name='class-delete'),

    re_path(r'^(?P<class_name>[-\w]+)/addstudent/$', views.ClassDetailStudentCreate.as_view(), name='class-student-create'),
    path('deletestudent/<int:pk>', views.ClassDetailStudentDelete.as_view(), name='class-student-delete'),
    path('updatestudent/<int:pk>', views.ClassDetailStudentUpdate.as_view(), name='class-student-update'),
]