from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,  blank=True, null=True , choices=(('Unpaid', 'Unpaid'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')))

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer.name}"