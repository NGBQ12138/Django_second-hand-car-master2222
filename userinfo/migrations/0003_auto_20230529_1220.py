# Generated by Django 2.1.1 on 2023-05-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20230522_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.BooleanField(choices=[('0', '男'), ('1', '女')], default='0', max_length=10, verbose_name='性别'),
        ),
    ]
