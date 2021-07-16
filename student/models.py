from datetime import date

import django.utils.timezone
from django.db import models

# Create your models here.
from django.urls import reverse

from classes.models import Class


class Student(models.Model):
    GENDER_CHOICES = (
        ('Nam', 'Nam'),
        ('Nu', 'Nu'),
        ('Khac', 'Khac'),
    )

    student_lastname = models.CharField('Ho va ten dem', max_length=80)
    student_firstname = models.CharField('Ten', max_length=50)
    student_gender = models.CharField('Gioi tinh', max_length=10, choices=GENDER_CHOICES, blank=True, default='Nam')
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, verbose_name='Lop')
    student_email = models.EmailField('Email', blank=True)
    student_date_of_birth = models.DateField('Ngay sinh', default=django.utils.timezone.now)
    student_reg = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['student_class', 'student_firstname']

    def __str__(self):
        return f'{self.student_lastname} {self.student_firstname}'

    def get_absolute_url(self):
        """Returns the url to access a particular classes instance."""
        return reverse('students:student-detail', args=[str(self.id)])
