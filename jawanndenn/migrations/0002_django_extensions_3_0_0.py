# Generated by Django 3.1 on 2020-08-15 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jawanndenn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ballot',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'get_latest_by': 'modified'},
        ),
    ]
