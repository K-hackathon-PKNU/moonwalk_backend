# Generated by Django 4.2.3 on 2023-09-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_delete_course_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='COURS_LT_CN',
        ),
        migrations.RemoveField(
            model_name='course',
            name='CVNTL_NM',
        ),
        migrations.RemoveField(
            model_name='course',
            name='OPTN_DC',
        ),
        migrations.AlterField(
            model_name='course',
            name='COURS_DETAIL_LT_CN',
            field=models.IntegerField(default=0),
        ),
    ]