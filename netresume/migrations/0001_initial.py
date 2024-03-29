# Generated by Django 5.0.3 on 2024-03-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=40)),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
            ],
        ),
    ]