# Generated by Django 3.2.8 on 2021-11-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20211125_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollowing',
            name='following',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='user',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
