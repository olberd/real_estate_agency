# Generated by Django 2.2.24 on 2022-12-13 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_claim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='author',
            new_name='user',
        ),
    ]
