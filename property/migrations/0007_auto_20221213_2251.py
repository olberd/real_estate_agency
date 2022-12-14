# Generated by Django 2.2.24 on 2022-12-13 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_auto_20221213_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='who_liked',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='property.Flat', verbose_name='Квартира на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
