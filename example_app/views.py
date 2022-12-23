from re import A
from urllib.request import Request
from django.shortcuts import render
from example_app.models import AboutUsModels

def index(request):
    form = Submit(request.POST)
    data = AboutUsModels.objects.all()
    if request.method == "POST":
        form = Submit(request)
        context = {'questions': data}
        return render(request, 'test.html', context)
