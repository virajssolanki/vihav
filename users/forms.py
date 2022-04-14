from django import forms
from .models import User, Profile, Bank
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from referral.models import Referrals, Withdraw
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

IAM_CHOICES = (
    ('Vihav\'s client', 'Vihav\'s client'),
    ('Vihav\'s employee', 'Vihav\'s employee'),
    ('Vendor or Suppliers', 'Vendor or Supplier'),
    ('Channel partner', 'Channel partner'),
    ('Other', 'Other'),
)

SITES = (
    ('KEYSTONE SKYVILLAS', 'KEYSTONE SKYVILLAS'),
    ('WEALTH SQUARE', 'WEALTH SQUARE'),
    ('VIHAV BUSINESS SQUARE', 'VIHAV BUSINESS SQUARE'),
    ('VIHAV SUPREMUS', 'VIHAV SUPREMUS'),
    ('VIHAV SKYONE', 'VIHAV SKYONE'),
    ('VIHAV TRADE CENTRE', 'VIHAV TRADE CENTRE'),
    ('VIHAV KEYSTONE MANSIONS', 'VIHAV KEYSTONE MANSIONS'),
    ('VIHAV KEYSTONE MANSIONS-2', 'VIHAV KEYSTONE MANSIONS-2'),
    ('VIHAV ELITE SQUARE', 'VIHAV ELITE SQUARE'),
    ('VIAHV EXCELUS', 'VIAHV EXCELUS'),
    ('VIHAV ENSIGN', 'VIHAV ENSIGN'),
)

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
	first_name = forms.CharField(widget= forms.TextInput(attrs={'class':'some_class','id':'some_id'}))
	last_name = forms.CharField(required=True)
	adress = forms.CharField(required=True)
	contact_number = forms.CharField(required=True)
	i_am = forms.ChoiceField(required=True, choices=IAM_CHOICES)
	sites = forms.ChoiceField(required=False, choices=SITES, widget= forms.Select(attrs={'id':'select', 'class':'select-field'}))

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'contact_number', 'email', 'adress',  'i_am', 'sites', 'password1', 'password2']
		widgets = {
			'email' : forms.TextInput(attrs = {'placeholder': 'enter your enail adress'}),
			}
			
	def clean(self):
		super(UserRegisterForm, self).clean()
		number = self.cleaned_data.get('contact_number')

		if len(number) > 10:
			self._errors['number'] = self.error_class(
				['please enter valid mobile number without country code'])
		return self.cleaned_data

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

	def clean(self):
		super(ProfileUpdateForm, self).clean()
		number = self.cleaned_data.get('number')

		if len(number) > 10:
			self._errors['number'] = self.error_class(
				['please enter valid mobile number without country code'])
		return self.cleaned_data

class MemberAcceptForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['credit', 'membership']
	def __init__(self, *args, **kwargs):
		super(MemberAcceptForm, self).__init__(*args, **kwargs)
		self.fields['credit'].label = "Welcome Credit"

class BankUpdateForm(forms.ModelForm):

	class Meta:
		model = Bank
		fields = ['account_holder_name', 'bank_name', 'account_number', 'IFSC_code', 'branch', 'account_type']

class NewReferral(forms.ModelForm):

	class Meta:
		model = Referrals
		fields = ['name', 'last_name', 'contact_number', 'email', 'city', 'site']

class NewAdminReferral(forms.ModelForm):
	reference_email = forms.EmailField()
	class Meta:
		model = Referrals
		fields = ['name', 'last_name', 'contact_number', 'email', 'city', 'reference_email']

class UpdateReferral(forms.ModelForm):
	class Meta:
		model = Referrals
		fields = ['name', 'contact_number', 'email', 'city', 'status', 'amount','note']
	def __init__(self, *args, **kwargs):
		super(UpdateReferral, self).__init__(*args, **kwargs)
		self.fields['note'].widget.attrs['rows'] = 5

class ContactUsForm(forms.Form):
	Subject = forms.CharField(required=True)
	Message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}),required=True)

class UpdateWithdraw(forms.ModelForm):
	class Meta:
		model = Withdraw
		fields = ['amount', 'status', 'holder', 'note']
	def __init__(self, *args, **kwargs):
		super(UpdateWithdraw, self).__init__(*args, **kwargs)
		self.fields['note'].widget.attrs['cols'] = 10
		self.fields['note'].widget.attrs['rows'] = 1