# Generated by Django 4.2.5 on 2023-10-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('adres', models.CharField(max_length=200)),
            ],
        ),
    ]
