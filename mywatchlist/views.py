from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# import mywatchlist.models
from mywatchlist.models import MyWatchListItem

# main HTML function
def mywatchlistitem_html(request):
    data = MyWatchListItem.objects.all()

    # data that will be passed to the HTML (in dictionary)
    context = {
        'name': 'Dylan Dahran Pribadi',
        'student_id': '2106720872',
        'items': data
    }
    return render(
        request,
        'mywatchlist.html',
        context
    )
    ...

# request data in the form of xml
def mywatchlistitem_xml(request):
    data = MyWatchListItem.objects.all()

    #return HttpResponse to provide an inbound HTTP request to a Django app with a text response
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
        )
    ...

# request data in the form of json
def mywatchlistitem_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(
        serializers.serialize("jason", data),
        content_type="application/json"
    )
    ...