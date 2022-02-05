# Generated by Django 4.0.2 on 2022-02-05 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_delete_contactuser_delete_task'),
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
        migrations.CreateModel(
            name='task',
            fields=[
                ('sno', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('Task', models.CharField(max_length=30)),
                ('Task_Description', models.TextField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]