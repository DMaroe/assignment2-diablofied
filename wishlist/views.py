from multiprocessing import context
from django.shortcuts import render
from wishlist.models import ItemWishlist

# Create your views here.
def show_wishlist(request):
    
    data_wishlist_item = ItemWishlist.objects.all()
    context = {
    'list_item': data_wishlist_item,
    'name': 'Dylan'
    }
    return render(request, "wishlist.html", context)

def index(request):

    return render(request, "index.html")
    ...