# Generated by Django 4.2.7 on 2023-11-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_informations_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='educations',
        ),
        migrations.DeleteModel(
            name='experiences',
        ),
        migrations.DeleteModel(
            name='informations',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='skills',
        ),
        migrations.DeleteModel(
            name='Testimonials',
        ),
    ]
