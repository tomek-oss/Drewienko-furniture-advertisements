# Generated by Django 3.1.3 on 2020-11-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201113_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default-avatar.jpg', upload_to='media_files/avatars'),
        ),
    ]