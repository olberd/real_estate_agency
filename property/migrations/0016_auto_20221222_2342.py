# Generated by Django 2.2.28 on 2022-12-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20221222_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='flat',
        ),
        migrations.AddField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]