from django.urls import path
from .views import happyCoders

urlpatterns = [
    path('', happyCoders, name='happyCoders'),
]
