# Generated by Django 3.1 on 2020-08-18 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200817_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='listing_winner', to=settings.AUTH_USER_MODEL),
        ),
    ]