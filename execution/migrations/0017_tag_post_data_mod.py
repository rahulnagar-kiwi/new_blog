# Generated by Django 2.0.1 on 2019-11-20 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0016_tag_post_user_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag_post',
            name='data_mod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='execution.Data'),
        ),
    ]
