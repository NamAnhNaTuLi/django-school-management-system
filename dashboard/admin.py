from django.contrib import admin

# Register your models here.
from classes.models import Class
from result.models import SubjectScore
from student.models import Student
from subjects.models import Subject, Khoa
from teachers.models import Teacher


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Khoa)
admin.site.register(SubjectScore)

