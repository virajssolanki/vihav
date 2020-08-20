from django import forms
from .models import User, Profile, Bank
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from referral.models import Referrals

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
	name = forms.CharField(required=True)
	city = forms.CharField(required=True)
	number = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ['name', 'city', 'email', 'number', 'password1', 'password2']
		widgets = {
			'username' : forms.TextInput(attrs = {'placeholder': 'enter your enail adress'}),
			}

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
	name = forms.CharField(required=True)
	city = forms.CharField(required=True)
	number = forms.CharField(required=True)

	class Meta:
		model = Profile
		fields = ['name', 'city', 'number']

class BankUpdateForm(forms.ModelForm):

	class Meta:
		model = Bank
		fields = ['account_holder_name', 'bank_name', 'account_number', 'IFSC_code', 'branch', 'account_type']

class NewReferral(forms.ModelForm):

	class Meta:
		model = Referrals
		fields = ['name', 'contact_number', 'email', 'location']