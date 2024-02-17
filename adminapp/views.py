from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from .models import Invoice
from django.http import HttpResponse

# Create your views here.
def adminportal(request):
    total_customers = Customer.objects.count()
  

    tot_inv=Invoice.objects.count()
    return render(request, 'adminportal.html',{'tot_cust':total_customers,'total_inv':tot_inv})

def createcustomer(request):
    total_customers = Customer.objects.count()
    if total_customers:
        tot_cust=total_customers+1
    else:
        tot_cust=1
    return render(request, 'createadmin.html',{'tot_cust':tot_cust})
def loginadmin(request):
  return render(request, 'login.html')


def loginn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminportal')
            else:
                login(request, user)
                messages.info(request, 'Please add admin username and password')
                return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password. Try again')
            return redirect('loginadmin')  # Redirect to the login page
    else:
        return redirect('loginadmin')
    

def customer_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        customer_id = request.POST.get('custid')
        email = request.POST.get('emailAddress')
        phone_number = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        
        # Create and save the Customer object
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            customer_id=customer_id,
            email=email,
            phone_number=phone_number,
            address=address
        )
        customer.save()
        return redirect('customer_list')
    else:
        return render(request,'customerlist.html')
    
def customer_list(request):
    customer=Customer.objects.all()
    return render(request,'customerlist.html',{'cust':customer})


def invoice_create(request):
    customer=Customer.objects.all()
    inv=Invoice.objects.count()
    if inv:
        invoice=inv+1
    else:
        invoice=1


    return render(request,'invoicecreate.html',{'cust':customer,'invc':invoice})


def edit_customer(request, id):
    
    if request.method == 'POST':
        # Get the customer object to edit
        customer = Customer.objects.get(id=id)

        # Update the customer object with the new data from the form
        customer.first_name = request.POST.get('firstName')
        customer.last_name = request.POST.get('lastName')
        customer.email = request.POST.get('emailAddress')
        customer.phone_number = request.POST.get('phoneNumber')
        customer.address = request.POST.get('address')

        # Save the updated customer object
        customer.save()

        # Redirect to a success page or any other appropriate page
        return redirect('customer_list')

    else:
        # If it's not a POST request, simply render the edit customer form
        customer = Customer.objects.get(id=id)
        context = {'cust': customer}
        return render(request, 'editcustomer.html', context)
    
    




def create_invoice(request):
    if request.method == 'POST':
        cust_id = request.POST.get('custname') 
        customer = Customer.objects.get(id=cust_id)
        inv_id=request.POST.get('invid') 
        date = request.POST.get('date')
        amount = request.POST.get('Amount')  
        status = request.POST.get('status') 
        invoice=Invoice.objects.create(
            customername=customer,
            invoice_id=inv_id,
            date=date,
            amount=amount,
            status=status
        )
        invoice.save()
        return redirect('invoicelist')
    else:
        return render(request, 'invoicelist.html')
    
def invoicelist(request):
    customer=Customer.objects.all()
    invoices = Invoice.objects.all()

    context={
        'cust':customer,
        'invoice':invoices
    }
    return render(request, 'invoicelist.html',context)

def editinvoice(request, id):
    # Retrieve the Invoice object from the database
    invoice = get_object_or_404(Invoice, id=id)
    
    if request.method == 'POST':
        # Retrieve form data
        invoice_date = request.POST.get('date')
        invoice_amount = request.POST.get('Amount')
        invoice_status = request.POST.get('status')
        
        # Update invoice details
        invoice.date = invoice_date
        invoice.amount = invoice_amount
        invoice.status = invoice_status
        invoice.save()
        
        return redirect('invoicelist')
    
    # Pass the Invoice object to the template for rendering the form
    return render(request, 'editinvoice.html', {'invoice': invoice})


# def invoice_edit(request,id):
#     if request.method == 'POST':
        
#         customer_id = request.POST.get('custname')
#         invoice_date = request.POST.get('date')
#         invoice_amount = request.POST.get('Amount')
#         invoice_status = request.POST.get('status')
        
#         # Retrieve the invoice object from the database using try-except block
#         try:
#             invoice = Invoice.objects.get(id=id)
#             # Update invoice details
#             invoice.customername_id = customer_id
#             invoice.date = invoice_date
#             invoice.amount = invoice_amount
#             invoice.status = invoice_status
#             invoice.save()
#             return redirect('invoicelist')
#         except Invoice.DoesNotExist:
#             # Handle the case when invoice with given ID does not exist
#             return HttpResponse("Invoice does not exist")

#     return render(request, 'editinvoice.html')


def logout(request):
    request.session['userid']=""
    auth.logout(request)
    return redirect('loginadmin')






    

    



   

