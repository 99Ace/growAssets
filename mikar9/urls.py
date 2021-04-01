from django.urls import path
from .views import mikar9, m9_create

urlpatterns = [
    path('', mikar9, name='mikar9'),
    path('m9_create', m9_create, name='m9_create'),
]
