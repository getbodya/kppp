# Generated by Django 2.1.1 on 2018-09-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absapp', '0010_abstract_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='all_rate',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
