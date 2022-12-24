# Generated by Django 2.2.28 on 2022-12-21 20:21
import phonenumbers
from django.db import migrations


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phone):
            flat.owner_pure_phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


def empty_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221221_2318'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, empty_owner_pure_phone)
    ]
