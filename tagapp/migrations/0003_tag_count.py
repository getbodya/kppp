# Generated by Django 2.1.1 on 2018-10-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagapp', '0002_remove_tag_conspects'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
