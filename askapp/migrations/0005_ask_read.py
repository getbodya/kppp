# Generated by Django 2.1.1 on 2018-10-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0004_ask_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
