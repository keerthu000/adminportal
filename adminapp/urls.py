from django.urls import path,include
from . import views
urlpatterns=[

path('',views.loginadmin,name='loginadmin'),
path('loginn',views.loginn,name="loginn"),

path('adminportal',views.adminportal,name='adminportal'),
path('createcustomer',views.createcustomer,name='createcustomer'),
path('customer_create',views.customer_create,name="customer_create"),
path('customer_list',views.customer_list,name="customer_list"),
path('invoice_create',views.invoice_create,name="invoice_create"),
path('create_invoice',views.create_invoice,name='create_invoice'),
path('invoicelist',views.invoicelist,name='invoicelist'),
path('editinvoice/<int:id>/', views.editinvoice, name="editinvoice"),
# path('invoice_edit/<int:id>/',views.invoice_edit,name="invoice_edit"),
path('edit_customer/<int:id>/',views.edit_customer,name="edit_customer"),
path('logout',views.logout,name='logout'),

    
]
