from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = [
            ('Fashion', 'Fashion'),
            ('Toys', 'Toys'),
            ('Electronics', 'Electronics'),
            ('Home', 'Home'),
            ('Pet', 'Pet'),
            ('Kitchen', 'Kitchen'),
            ('Other','Other')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image_url = models.URLField(blank=True)
    initial_bid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    category = models.CharField(blank=True, choices=CATEGORIES, max_length=64)
    creation_time = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    active = models.BooleanField(default=True)
    max_bid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    saved = models.ManyToManyField(User, blank=True, related_name="favorites")
    winner = models.ForeignKey(User, null=True, default=None, on_delete=models.PROTECT, related_name="winning_listings")

    def __str__(self):
        return self.title

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    bid = models.DecimalField(max_digits=12, decimal_places=2)
    bid_time = models.DateTimeField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")

    def __str__(self):
        return f"User {self.bidder} bid: ${self.bid}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return f"User {self.user} comment on listing {self.listing} on {self.date}"