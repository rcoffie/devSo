# Generated by Django 3.2 on 2022-12-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default.jpeg', null=True, upload_to='profiles/'),
        ),
    ]
