# Generated by Django 4.0.3 on 2022-10-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]