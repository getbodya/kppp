# Generated by Django 2.1.1 on 2018-10-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagapp', '0004_remove_tag_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
