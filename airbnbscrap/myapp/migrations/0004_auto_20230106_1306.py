# Generated by Django 3.2 on 2023-01-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_airbnbdata_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airbnbdata',
            name='Hosted_By',
        ),
        migrations.RemoveField(
            model_name='airbnbdata',
            name='HouseRule',
        ),
    ]
