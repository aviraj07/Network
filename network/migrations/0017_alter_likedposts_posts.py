# Generated by Django 3.2.8 on 2021-11-28 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_alter_likedposts_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedposts',
            name='posts',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.post'),
        ),
    ]
