# Generated by Django 3.1 on 2020-08-12 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200812_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_bids', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_comments', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
