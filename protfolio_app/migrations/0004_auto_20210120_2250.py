# Generated by Django 3.0.5 on 2021-01-20 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio_app', '0003_auto_20210120_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience_project',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience_project',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
