from django.db import models

# Create your models here.
from django.urls import reverse

from teachers.models import Teacher


class Class(models.Model):
    class_name = models.CharField('Lop', max_length=50, unique=True, error_messages={'unique':"Lop hoc nay da ton tai"})
    giao_vien_CN = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Giao vien CN')

    class Meta:
        ordering = ['class_name']

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        """Returns the url to access a particular classes instance."""
        return reverse('classes:class-detail', args=[str(self.class_name)])