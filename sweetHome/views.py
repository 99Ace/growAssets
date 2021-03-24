from django.shortcuts import render, HttpResponse, redirect, reverse
import pymongo
import os

# Setting up the MONGODB DATABASES to be link up
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'GrowAssets'
COLLECTION_NAME = 'sweetExpenses'

# set up the connection to MONGO_URI which we set up in bashrc
conn = pymongo.MongoClient(MONGO_URI)
# set 'data' to be the name to represent the database link
data = conn[DATABASE_NAME][COLLECTION_NAME]

# Create your views here.


def sweethome(request):

    return HttpResponse("Sweet Home")


def new_expenses(request):
    if request.method == "POST":
        print(request.POST['description'])
        return redirect(reverse(sweethome))

    return render(request, 'new_expenses.html')
