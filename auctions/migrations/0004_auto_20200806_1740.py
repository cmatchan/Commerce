# Generated by Django 3.0.8 on 2020-08-07 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200802_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='price',
        ),
    ]
