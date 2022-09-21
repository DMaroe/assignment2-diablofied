from django.shortcuts import render

from katalog.models import CatalogItem

def request_catalogs(request):
    data = CatalogItem.objects.all()

    # data yang mau dipass ke html
    context = {
        'name' : 'dylan pinter',
        'student_id' : 2106720872,
        'catalogs' : data
    }

    # bakal ngerender data ke html
    # data mapping
    return render(
        request,
        'katalog.html',
        context,
    )
