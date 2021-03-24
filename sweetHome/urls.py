from django.urls import path
from .views import sweethome

urlpatterns = [
    path('', sweethome, name='sweethome'),
]
