# Generated by Django 4.2.3 on 2023-10-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_remove_runningmate_rm_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningmate',
            name='Rm_level',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterModelTable(
            name='runningmate',
            table='Runningmate',
        ),
    ]