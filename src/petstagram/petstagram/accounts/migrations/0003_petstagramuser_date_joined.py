# Generated by Django 3.2.4 on 2021-07-21 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_petstagramuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstagramuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
