from django.shortcuts import render
from .forms import NewInvoice
from .models import Invoice
import datetime
# from datetime import date, timedelta

# Create your views here.


def mikar9(request):
    data = Invoice.objects.all()
    return render(request, 'mikar9/index.html', {
        'data':data
    })


def m9_create(request):
    if request.method == "POST":
        new_entry = NewInvoice(request.POST)
        if new_entry.is_valid():
            instance = new_entry.save(commit=False)
            
            inv_date = request.POST.get('inv_date')
            new_entry.inv_date = datetime.datetime.strptime(
                inv_date, '%Y-%m-%d'
            )
            instance.inv_date = inv_date
            # USERNAME
            instance.user = request.user
            print(instance.user)
            # YEAR
            print(new_entry.inv_date.year)
            instance.financial_year = new_entry.inv_date.year
            # MONTH
            print(new_entry.inv_date.month)
            instance.month = new_entry.inv_date.month
            # DAY
            print(new_entry.inv_date.day)

            # store log data
            # instance.save()
            print("Log is saved")

    form = NewInvoice()
    return render(request, 'mikar9/m9_create.html', {
        'form': form
    })
