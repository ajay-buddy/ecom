# Generated by Django 2.2.13 on 2020-11-28 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
