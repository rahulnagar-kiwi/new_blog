# Generated by Django 2.0.1 on 2019-11-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0018_auto_20191120_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='pub_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
