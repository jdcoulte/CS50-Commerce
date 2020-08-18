from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<int:listing_id>", views.listing, name="listing"),
    path("bid", views.bid, name="bid"),
    path("close", views.close, name="close"),
    path("open", views.open, name="open"),
    path("add", views.add, name="add"),
    path("remove", views.remove, name="remove"),
    path("comment", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.category, name="category")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
