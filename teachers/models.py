from django.db import models

# Create your models here.
from django.urls import reverse

from subjects.models import Subject, Khoa


class Teacher(models.Model):
    name = models.CharField('Ten giao vien', max_length=300)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, null=True)
    bo_mon = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['khoa', 'bo_mon', 'name']

    def __str__(self):
        return self.name

    # def cac_lop(self):
    #     return ', '.join(lop.lop for lop in self.lop_phu_trach.all())
    #
    # cac_lop.short_description = 'Lop phu trach'

    def get_absolute_url(self):
        return reverse('teachers:teacher-detail', args=[str(self.id)])