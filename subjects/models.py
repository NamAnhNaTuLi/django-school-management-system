from django.db import models


# Create your models here.


class Subject(models.Model):
    subject = models.CharField('Ten mon hoc', max_length=40, unique=True, error_messages={'unique':"Mon hoc nay da ton tai"})
    subject_unit = models.IntegerField('So tiet hoc', blank=True, null=True)

    def __str__(self):
        return self.subject


class Khoa(models.Model):
    department = models.CharField('Ten khoa', max_length=40, unique=True, error_messages={'unique':"Khoa nay da ton tai"})

    def __str__(self):
        return self.department
