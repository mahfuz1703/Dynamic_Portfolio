# Generated by Django 5.0.6 on 2024-06-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('gmail', models.CharField(blank=True, max_length=100)),
                ('experience', models.CharField(blank=True, max_length=100)),
                ('language', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
