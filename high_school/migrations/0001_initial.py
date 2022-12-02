# Generated by Django 3.2 on 2022-12-02 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('class_name', models.CharField(choices=[('a', 'a_class'), ('b', 'b_class'), ('c', 'c_class')], max_length=30, verbose_name='Название класса')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('birth_date', models.DateField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='high_school.teacher')),
            ],
        ),
    ]