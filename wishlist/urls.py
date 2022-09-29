from django.urls import path
from wishlist.views import show_wishlist, index

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('index/', index, name="index")
]