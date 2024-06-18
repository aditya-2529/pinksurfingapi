# Generated by Django 5.0.6 on 2024-06-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_login_message_login_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='Email', max_length=100)),
                ('password', models.CharField(default='Password', max_length=50)),
                ('status', models.CharField(default='success', max_length=10)),
                ('message', models.CharField(default='200 OK', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
