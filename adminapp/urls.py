from django.urls import path,include
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy, InvoiceListCreate, InvoiceRetrieveUpdateDestroy
from . import views
urlpatterns=[

# path('',views.loginadmin,name='loginadmin'),
# path('loginn',views.loginn,name="loginn"),

# path('adminportal',views.adminportal,name='adminportal'),
# path('createcustomer',views.createcustomer,name='createcustomer'),
# path('customer_create',views.customer_create,name="customer_create"),
# path('customer_list',views.customer_list,name="customer_list"),
# path('invoice_create',views.invoice_create,name="invoice_create"),
# path('create_invoice',views.create_invoice,name='create_invoice'),
# path('invoicelist',views.invoicelist,name='invoicelist'),
# path('editinvoice/<int:id>/', views.editinvoice, name="editinvoice"),
# path('invoice_edit/<int:id>/',views.invoice_edit,name="invoice_edit"),
# path('edit_customer/<int:id>/',views.edit_customer,name="edit_customer"),
# path('get_customer_invoice_data/', views.get_customer_invoice_data, name='get_customer_invoice_data'),
# path('customer_and_invoice_view/', views.customer_and_invoice_view, name='customer_and_invoice_view'),
# path('logout',views.logout,name='logout'),
path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
path('invoices/', InvoiceListCreate.as_view(), name='invoice-list-create'),
path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroy.as_view(), name='invoice-detail'),

    
]
