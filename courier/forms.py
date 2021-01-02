from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateContainerForm(ModelForm):
	
	class Meta:
		model = Container
		fields = '__all__'
		widgets = {
			'container_no': forms.TextInput(attrs={'class':'form-control'}),
			'cont_status': forms.Select(attrs={'class':'form-control'}),
			}


class CreateCustomerForm(forms.ModelForm):
	

	class Meta:
		model = Customer
		fields = ['name','phone','pieces','status']
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),
			'pieces': forms.TextInput(attrs={'class':'form-control'}),
			'container': forms.TextInput(attrs={'class':'form-control'}),
			'status': forms.Select(attrs={'class':'form-control'}),
		}

class UpdateCustomerForm(forms.ModelForm):
	

	class Meta:
		model = Customer
		fields = ['status']
		widgets = {
			
			'status': forms.Select(attrs={'class':'form-control'}),
		}

class UpdateContainerForm(ModelForm):
	
	class Meta:
		model = Container
		fields = ['cont_status']
		widgets = {
			'container_no': forms.TextInput(attrs={'class':'form-control'}),
			'cont_status': forms.Select(attrs={'class':'form-control'}),
			}

		
class SelectCustomersForm(forms.ModelForm):

	class Meta:
		model= Customer
		fields = '__all__'



class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = User
		
		fields = ['username','email','password1','password2']

		
