# Generated by Django 4.2.7 on 2023-11-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_coding_skill_design_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('item_no', models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth')], max_length=300)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
