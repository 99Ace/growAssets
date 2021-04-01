from django.shortcuts import render

# Create your views here.
def mikar9(request):
    return render(request, 'mikar9/index.html')


def m9_create(request):
    return render(request, 'mikar9/m9_create.html')