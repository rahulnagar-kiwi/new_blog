# Generated by Django 2.0.1 on 2019-11-18 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0009_auto_20191115_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
