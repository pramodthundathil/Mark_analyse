# Generated by Django 5.0.6 on 2025-04-10 08:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20230411_1743'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('exam_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='mark_exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('marks', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='predict.examination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_mark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
