# Generated by Django 4.2.7 on 2023-11-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_educations_experiences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educations',
            name='ending_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='educations',
            name='starting_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='level',
            field=models.IntegerField(),
        ),
    ]
