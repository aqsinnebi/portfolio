# Generated by Django 4.2.5 on 2023-10-01 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_rename_adres_contact_adr_rename_phone_contact_phn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='adr',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='eml',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phn',
            new_name='phone',
        ),
    ]
