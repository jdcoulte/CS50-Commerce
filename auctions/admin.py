from django.contrib import admin
from .models import User, Listing, Bid, Comment

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass