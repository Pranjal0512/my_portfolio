# Generated by Django 4.2.7 on 2023-11-10 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_coding_skill_design_skill'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coding_Skill',
        ),
        migrations.DeleteModel(
            name='Design_Skill',
        ),
    ]
