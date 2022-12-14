# Generated by Django 2.2.28 on 2022-12-22 20:43

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        flats = Flat.objects.filter(owner=owner.owner, owners_phonenumber=owner.owners_phonenumber)
        if flats:
            owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20221222_2342'),
    ]

    operations = [
        migrations.RunPython(copy_owners, )
    ]
