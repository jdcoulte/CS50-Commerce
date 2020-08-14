from django.forms import ModelForm, Form
from .models import Listing, Bid

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'image_url', 'initial_bid', 'category']
        labels = {
            'title': "Listing Title:",
            'description': "Description\n(max 1,000 characters):",
            'image_url': "Image URL:",
            'initial_bid': "Initial Bid ($):",
            'category': "Category (Choose one):"
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']