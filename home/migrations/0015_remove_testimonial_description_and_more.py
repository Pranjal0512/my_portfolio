# Generated by Django 4.2.7 on 2023-11-10 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_education_experience_information_service_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='Post',
        ),
    ]
