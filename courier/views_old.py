from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models  import *
from .forms import CreateUserForm
from .forms import CreateContainerForm
from .forms import CreateCustomerForm
from django.contrib import messages




# Create your views here.
def register(request):
	form =CreateUserForm()


	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context={'form':form}
	return render(request,'register.html',context)
def login(request):
	return render(request,'login.html')



def container(request):
	containers = Container.objects.all()
	return render(request,'container.html',{'containers':containers})
def allcustomers(request):
	allcustomers = Customer.objects.all()
	return render(request,'allcustomers.html',{'allcustomers':allcustomers})

def containerpages(request,pk_test):
	containers = Container.objects.get(id=pk_test)
	customers =containers.customer_set.all()
	context={'containers':containers,'customers':customers}
	return render(request,'containerpages.html',context)

def createContainer(request):

	form=CreateContainerForm()
	if request.method == 'POST':
		print("printing POST : ",request.POST)
		form=CreateContainerForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/container')

	context = {'form':form}
	return render(request,'create-containerform.html',context)

def updateContainer(request,pk_cont):
	container=Container.objects.get(id=pk_cont)
	customers =container.customer_set.all()
	form=CreateContainerForm(instance=container)
	if request.method=='POST':
		form=CreateContainerForm(request.POST,instance=container)
		if form.is_valid:
			form.save()
			
			customers.update(status=container.cont_status)
			for i in customers:
				print("status '{}' is sent to {}".format(i.status,i.phone))
			return redirect('/container')

	context={'form':form}
	return render(request,'create-containerform.html',context)



def createCustomer(request,cont_id):
	
	form =CreateCustomerForm(initial={'container':cont_id})
	if request.method == 'POST':
		print('printing the POST : ',request.POST)
		form =CreateCustomerForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/container')

	context={'form':form}
	return render(request,'create-customerform.html',context)

def updateCustomer(request,pk):

	customer=Customer.objects.get(id=pk)
	form =CreateCustomerForm(instance=customer)

	if request.method == 'POST':
		
		form =CreateCustomerForm(request.POST,instance=customer)
		if form.is_valid:
			form.save()

			return redirect('/container')


	context={'form':form}
	return render(request,'create-customerform.html',context)

def deleteCustomer(request,pk_del):

	customer=Customer.objects.get(id=pk_del)
	if request.method=="POST":
		customer.delete()
		return redirect('/container')
	context={'customer':customer}
	return render(request,'delete-customer.html',context)

def deleteContainer(request,pk_del_cont):

	container=Container.objects.get(id=pk_del_cont)
	if request.method=="POST":
		container.delete()
		return redirect('/container')
	context={'container':container}
	return render(request,'delete-container.html',context)



