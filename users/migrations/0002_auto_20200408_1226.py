# Generated by Django 3.0.3 on 2020-04-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('JSY', 'Jersey'), ('GSY', 'Guernsey'), ('ADY', 'Alderny'), ('SARK', 'Sark'), ('HERM', 'Herm')], max_length=20),
        ),
    ]
