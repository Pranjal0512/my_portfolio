# Generated by Django 4.2.7 on 2023-11-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('phone', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
            ],
        ),
    ]
