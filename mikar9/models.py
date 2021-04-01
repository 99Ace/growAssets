from django.db import models

# Create your models here.
class Invoice(models.Model):
    # Description of the expenses
    invoice = models.CharField(
        max_length=50,
        blank=False
    )
    # Tag to a carplate else set to admin
    car_plate = models.CharField(
        max_length=8,
    )
    # Accounts Receivable
    accounts_receivables = models.DecimalField(
        blank=False,
        max_digits=7,
        decimal_places=2
    )
    # Credit/Debit
    BALANCE = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    balance = models.CharField(
        max_length=6,
        choices=BALANCE,
        blank=False,
    )
    # Accounts Payable
    accounts_payable = models.CharField(
        max_length=50,
        blank=False,
    )
    # Invoice Date
    inv_date = models.DateField()

    # AUTO ADD THE CREATION DATE
    log_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.invoice + " [" + self.car_plate + ']')