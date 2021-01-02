from django.urls import path
from . import views


urlpatterns = [
	path('register/',views.register, name='register'),
	path('',views.loginPage, name='loginPage'),
	path('logoutUser/',views.logoutUser, name='logoutUser'),
	path('container/',views.container, name='container'),
	path('allcustomers/',views.allcustomers, name='allcustomers'),
	path('container/<str:pk_test>',views.containerpages, name='containerpages'),
	path('create_container/',views.createContainer,name='createContainer'),
	path('create_customer/',views.createCustomer,name='createCustomer'),
	path('create_groupcustomers/<str:ct_id>',views.createGroupCustomers,name='create-groupcustomers'),
	path('update_customer/<str:pk>',views.updateCustomer,name='updateCustomer'),
	path('update_container/<str:pk_cont>',views.updateContainer,name='updateContainer'),
	path('delete_customer/<str:pk_del>',views.deleteCustomer,name='deleteCustomer'),
	path('delete_container/<str:pk_del_cont>',views.deleteContainer,name='deleteContainer'),
	path('add_customer/',views.addcustomer, name='add_customer'),
	path('remove_all/',views.removeAll, name='removeAll'),
	
	
]