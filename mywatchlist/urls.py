from django.urls import path
from mywatchlist.views import mywatchlistitem_html,mywatchlistitem_xml,mywatchlistitem_json

app_name = "mywatchlist"

#routing url 
urlpatterns = [
    path('html/', mywatchlistitem_html, name='mywatchlistitem_html'),
    path('xml/', mywatchlistitem_xml, name="mywatchlistitem_xml"),
    path('json/', mywatchlistitem_json, name="mywatchlistitem_json")
]   