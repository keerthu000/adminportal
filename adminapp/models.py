from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

class Invoice(models.Model):
    customername=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    invoice_id= models.CharField(max_length=100)
    date=models.DateField(null=True)
    amount=models.IntegerField()
    status=models.CharField(max_length=100)
