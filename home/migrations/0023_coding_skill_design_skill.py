# Generated by Django 4.2.7 on 2023-11-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_delete_coding_skill_delete_design_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coding_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('level', models.IntegerField()),
                ('color', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Design_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('level', models.IntegerField()),
                ('color', models.CharField(max_length=300)),
            ],
        ),
    ]
