# Generated by Django 3.2.8 on 2021-11-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20211124_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollowing',
            name='following_user_id',
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='following',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='user',
            field=models.CharField(default=0, max_length=64),
        ),
    ]