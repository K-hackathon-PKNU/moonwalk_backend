# Generated by Django 4.2.3 on 2023-10-02 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rewards', '0001_initial'),
        ('login', '0005_delete_profile_alter_account_user_id_and_more'),
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='User_ID',
            field=models.ForeignKey(db_column='User_ID', default=0, on_delete=django.db.models.deletion.CASCADE, to='login.account'),
        ),
        migrations.AddField(
            model_name='user_info',
            name='nickname',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='residence',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='User_lev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rewards.reward'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='attendance',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
