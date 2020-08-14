from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import User, Listing, Bid, Comment
from .forms import ListingForm, BidForm

import datetime

def index(request):
    listings = Listing.objects.filter(active=True)
    watchlist = request.user.favorites.all()
    watchlistcount = len(watchlist)
    bid = {}
    for listing in listings:
        if listing.max_bid == 0:
            listing.max_bid = listing.initial_bid
    return render(request, "auctions/index.html", {
        "listings": listings,
        "watchlist": watchlist,
        "watchlistcount": watchlistcount,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required()
def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = Listing()
            listing.title = form.cleaned_data['title']
            listing.description = form.cleaned_data['description']
            listing.image_url = form.cleaned_data['image_url']
            listing.initial_bid = form.cleaned_data['initial_bid']
            listing.category = form.cleaned_data['category']
            listing.creation_time = datetime.datetime.now()
            listing.owner = request.user
            listing.active = True
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            form = ListingForm()
            return render(request, "auctions/create.html", {
                'form': form,
                'message': "Invalid listing. Please try again."
            })
    else:
        watchlist = request.user.favorites.all()
        watchlistcount = len(watchlist)
        return render(request, "auctions/create.html", {
            'form': ListingForm(),
            'watchlistcount': watchlistcount
        })

def listing(request, listing_id):
    # Pull the listing from the database.
    listing = Listing.objects.get(pk=listing_id)
    owner = listing.owner.username

    # Get a list of bids for the listing
    bids = Bid.objects.filter(listing=listing)
    bidcount = len(bids)
    
    # Check if the listing has any previous bids. If there haven't been any bids, max_bid will be 0 so it should be set the same as the initial bid.
    if listing.max_bid == 0:
        listing.max_bid = listing.initial_bid

    if request.user.is_authenticated:
        # Get a list of the logged-in user's favorites.
        favorites = request.user.favorites.all()
    
        # Check if the listing is in the user's list of favorites.
        favorite = listing in favorites # Will return true if the user has favorited the listing.

        # Get a count of listings the user has favorited (for the number displayed on the menu)
        watchlistcount = len(favorites)

        # Initialize the form for bidding
        form = BidForm()

        return render(request, "auctions/listing.html", {
            'listing': listing,
            'owner': owner,
            'bids': bids,
            'favorite': favorite,
            'watchlistcount': watchlistcount,
            'bidcount': bidcount,
            'form': form
        })
    else:
        return render(request, "auctions/listing.html", {
            'listing': listing,
            'owner': owner,
            'bids': bids,
            'bidcount': bidcount
        })

def bid(request, listing_id):
    if request.method == "POST":
        form = BidForm(request.POST)
        listing = Listing.objects.get(pk=listing_id)
        if listing.initial_bid > listing.max_bid:
            min_bid = listing.initial_bid
        else:
            min_bid = listing.max_bid

        if form.is_valid():
            bidamount = form.cleaned_data['bid']
            if bidamount >= min_bid:
                bid = Bid()
                bid.bid = bidamount
                bid.bidder = request.user
                bid.listing = listing
                bid.bid_time = datetime.datetime.now()
                bid.save()
                listing.max_bid = bidamount
                listing.save()
                link = "/listings/" + str(listing_id)
                return HttpResponseRedirect(link)

        message = "Invalid bid. Please return to the listing to try again."
        link = "/listings/" + str(listing_id)
        linktext = "Return to Listing"
        return render(request, "auctions/error.html", {
            'error': 'Bid Error',
            'message': message,
            'link': link,
            'linktext': linktext
        })
    else:
        url = "listing" + str(listing_id)
        # This is not currently working because it is trying to redirect to /bid/listing/listing_id. Need to figure out how to pass a parameter into the "reverse" function.
        return HttpResponseRedirect(url)