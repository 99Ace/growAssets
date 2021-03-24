from django.urls import path
from .views import sweethome, new_expenses

urlpatterns = [
    path('', sweethome, name='sweethome'),
    path('new_expenses/', new_expenses, name='new_expenses'),
]
