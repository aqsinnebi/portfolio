# Generated by Django 4.2.5 on 2023-10-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_rename_adr_contact_adres_rename_eml_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='update',
            field=models.TimeField(auto_now=True),
        ),
    ]
