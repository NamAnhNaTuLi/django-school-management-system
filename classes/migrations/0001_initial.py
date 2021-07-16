# Generated by Django 3.2.5 on 2021-07-14 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(error_messages={'unique': 'Lop hoc nay da ton tai'}, max_length=50, unique=True, verbose_name='Lop')),
                ('giao_vien_CN', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacher', verbose_name='Giao vien CN')),
            ],
            options={
                'ordering': ['class_name'],
            },
        ),
    ]
