from django.db import models

# Create your models here.
from student.models import Student
from subjects.models import Subject


def convert(x):
    return [float(i) for i in x.split()]


class SubjectScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Hoc sinh")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Mon hoc")
    diem_he_so_1 = models.CharField(max_length=40, blank=True)
    diem_he_so_2 = models.CharField(max_length=40, blank=True)
    diem_he_so_3 = models.CharField(max_length=40, blank=True)

    class Meta:
        unique_together = ('student', 'subject',)
        ordering = ['subject']

    def diemTB(self):
        if self.diem_he_so_1 and self.diem_he_so_2 and self.diem_he_so_3:
            return round((sum(convert(self.diem_he_so_1)) + sum(convert(self.diem_he_so_2)) * 2 + sum(convert(self.diem_he_so_3)) * 3) / (
                    len(convert(self.diem_he_so_1)) + len(convert(self.diem_he_so_2)) * 2 + len(convert(self.diem_he_so_3)) * 3),2)
        else:
            return ''

    def phanloai(self):
        if not self.diemTB():
            return ''
        elif self.diemTB() >= 8:
            return "Gioi"
        elif self.diemTB() >= 7:
            return "Kha"
        elif self.diemTB() >= 6:
            return "Trung binh"
        else:
            return "Yeu"

    def __str__(self):
        return f'{self.student}: Diem mon {self.subject}'

