# Generated by Django 4.0 on 2022-01-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]