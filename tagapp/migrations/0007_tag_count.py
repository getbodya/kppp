# Generated by Django 2.1.1 on 2018-10-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagapp', '0006_remove_tag_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
