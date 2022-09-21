from django.urls import path
from katalog.views import request_catalogs

appname = 'katalog'

urlpatterns = [
    path('', request_catalogs, name='request_catalogs')
]