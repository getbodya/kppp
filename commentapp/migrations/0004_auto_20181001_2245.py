# Generated by Django 2.1.1 on 2018-10-01 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0003_coment_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coment',
            old_name='author',
            new_name='user',
        ),
    ]
