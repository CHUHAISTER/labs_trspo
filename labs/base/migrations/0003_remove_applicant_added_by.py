# Generated by Django 5.0.6 on 2024-05-21 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_applicant_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='added_by',
        ),
    ]
