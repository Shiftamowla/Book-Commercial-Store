# Generated by Django 5.1 on 2025-01-20 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_remove_creatorprofilemodel_achievements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='viewersprofilemodel',
            name='user',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_link', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(default='https://via.placeholder.com/100x150')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myApp.author')),
            ],
        ),
        migrations.DeleteModel(
            name='creatorProfileModel',
        ),
        migrations.DeleteModel(
            name='customUser',
        ),
        migrations.DeleteModel(
            name='viewersProfileModel',
        ),
    ]
