from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from .models  import *
from .forms import CreateUserForm
from .forms import CreateContainerForm
from .forms import CreateCustomerForm
from .forms import UpdateCustomerForm
from .forms import UpdateContainerForm
from .forms import SelectCustomersForm
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required



#----------------------------send message------------------------------------>
def sendMessage(customer):

		account_sid = 'AC4b3116997693eac703a76a9f7166ea15'
		auth_token = 'b26a9d21d87ff733a92d5310e763b8c9'
		client = Client(account_sid, auth_token)

		message = client.messages.create(
		                     body=f'Dear Mr.{customer.name}  your package of {customer.pieces} pieces has been {customer.status} /n CargoTrack',
		                     from_='+19387661193',
		                     to={customer.phone}
		                 )

		print(message.sid)
#-------------------------send message ----------------------------------->

# Create your views here.
def register(request):
	form =CreateUserForm()


	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context={'form':form}
	return render(request,'register.html',context)
def loginPage(request):

	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')


		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('/allcustomers')
		else:
			messages.info(request,"Username or password is incorrect")

	context={}
	return render(request,'login.html',context)



def logoutUser(request):
	logout(request)
	return redirect('loginPage')


@login_required(login_url='loginPage')
def container(request):
	containers = Container.objects.all()
	return render(request,'container.html',{'containers':containers})


@login_required(login_url='loginPage')
def allcustomers(request):
	allcustomers = Customer.objects.all()
	return render(request,'allcustomers.html',{'allcustomers':allcustomers})


@login_required(login_url='loginPage')
def containerpages(request,pk_test):
	containers = Container.objects.get(id=pk_test)
	customers =containers.customer_set.all()
	context={'containers':containers,'customers':customers}
	return render(request,'containerpages.html',context)

@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
def updateContainer(request,pk_cont):
	container=Container.objects.get(id=pk_cont)
	customers =container.customer_set.all()
	form=UpdateContainerForm(instance=container,)
	if request.method=='POST':
		form=UpdateContainerForm(request.POST,instance=container)
		if form.is_valid:
			form.save()
			
			customers.update(status=container.cont_status)
			for i in customers:
				sendMessage(i)
			return redirect('/container')

	context={'form':form}
	return render(request,'create-containerform.html',context)


@login_required(login_url='loginPage')
def createCustomer(request):
	
	form =CreateCustomerForm()

	if request.method == 'POST':
		print('printing the POST : ',request.POST)
		
		form =CreateCustomerForm(request.POST)

		if form.is_valid:
			form.save()
			customer=Customer.objects.all().last()
			try:
				sendMessage(customer)
			except:
				Customer.objects.all().last().delete()
				messages.info(request,"The number is not active , please check the number again")
				return redirect('/create_customer')
				


			print("the customer is ",customer)
			return redirect('/allcustomers')


	context={'form':form}
	return render(request,'create-customerform.html',context)

@login_required(login_url='loginPage')
def updateCustomer(request,pk):

	customer=Customer.objects.get(id=pk)
	form =UpdateCustomerForm(instance=customer)

	if request.method == 'POST':
		
		form =UpdateCustomerForm(request.POST,instance=customer)
		if form.is_valid:
			form.save()
			sendMessage(customer)
			return redirect('/allcustomers')


	context={'form':form}
	return render(request,'create-customerform.html',context)

@login_required(login_url='loginPage')
def deleteCustomer(request,pk_del):

	customer=Customer.objects.get(id=pk_del)
	if request.method=="POST":
		customer.delete()
		return redirect('/allcustomers')
	context={'customer':customer}
	return render(request,'delete-customer.html',context)

@login_required(login_url='loginPage')
def deleteContainer(request,pk_del_cont):

	container=Container.objects.get(id=pk_del_cont)
	if request.method=="POST":
		container.delete()
		return redirect('/container')
	context={'container':container}
	return render(request,'delete-container.html',context)

@login_required(login_url='loginPage')
def createGroupCustomers(request,ct_id):
	container=Container.objects.get(id=ct_id)
	groupcustomers=Customer.objects.all()
	print('container id is ' ,ct_id)
	


	context={'groupcustomers':groupcustomers,'container':container}
	return render(request,'create-groupcustomers.html',context)


@login_required(login_url='loginPage')
def addcustomer(request):
	data =json.loads(request.body)
	customerId=data['customerId']
	action = data['action']
	containerId = data['containerId']
	
	print('customer is',customerId)
	print('action is',action)
	print('container is',containerId)
	customer=Customer.objects.get(id=customerId)
	containers=Container.objects.get(id=containerId)
	customer.container=containers
	customer.save()
	
	return JsonResponse('Customer was added to container',safe=False)


def removeAll(request):
	allcustomers=Customer.objects.all()
	if request.method == "POST":
			allcustomers.delete()
			return redirect('/allcustomers')
	context={'allcustomers':allcustomers}
	return render(request,'remove-all.html',context)







