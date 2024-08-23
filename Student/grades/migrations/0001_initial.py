# Generated by Django 5.1 on 2024-08-22 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_key', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_key', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('remarks', models.CharField(editable=False, max_length=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.subject')),
            ],
        ),
    ]
