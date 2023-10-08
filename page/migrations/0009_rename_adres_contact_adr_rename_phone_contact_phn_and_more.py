# Generated by Django 4.2.5 on 2023-10-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_alter_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='adres',
            new_name='adr',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='phn',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AddField(
            model_name='contact',
            name='eml',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]