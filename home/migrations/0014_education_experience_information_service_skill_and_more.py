# Generated by Django 4.2.7 on 2023-11-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_educations_delete_experiences_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('starting_year', models.IntegerField()),
                ('ending_year', models.IntegerField()),
                ('university', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('starting_year', models.IntegerField()),
                ('ending_year', models.IntegerField()),
                ('university', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('name', models.CharField(max_length=300)),
                ('Post', models.CharField(max_length=300)),
                ('Description', models.TextField()),
            ],
        ),
    ]
