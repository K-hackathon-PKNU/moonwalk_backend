# Generated by Django 4.2.3 on 2023-10-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_account_info_remove_account_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account_info',
        ),
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterModelTable(
            name='account',
            table='Account',
        ),
    ]