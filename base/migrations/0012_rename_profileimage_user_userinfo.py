# Generated by Django 5.0.6 on 2024-06-18 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_user_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profileImage',
            new_name='userInfo',
        ),
    ]