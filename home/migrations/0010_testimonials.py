# Generated by Django 4.2.7 on 2023-11-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=300)),
                ('Post', models.CharField(max_length=300)),
                ('Description', models.TextField()),
            ],
        ),
    ]
