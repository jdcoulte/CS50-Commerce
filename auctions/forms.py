from django.forms import ModelForm
from auctions.models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'image_url', 'initial_bid', 'category']
        labels = {
            'title': "Listing Title:",
            'description': "Description\n(max 100 characters):",
            'image_url': "Image URL:",
            'initial_bid': "Initial Bid ($):",
            'category': "Category (Choose one):"
        }