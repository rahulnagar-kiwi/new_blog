# Generated by Django 2.0.1 on 2019-11-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0014_auto_20191119_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag_post',
            name='user_tag',
        ),
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
