# Generated by Django 3.1 on 2020-08-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='max_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]