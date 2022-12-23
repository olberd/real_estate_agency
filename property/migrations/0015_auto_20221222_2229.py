# Generated by Django 2.2.28 on 2022-12-22 19:29

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    flats=flat.flat.id)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners, )
    ]
