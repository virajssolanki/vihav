from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User, Bank
from .models import Referrals, Withdraw
from users.forms import BankUpdateForm, NewReferral
# Create your views here.
def home(request):
	user=request.user
	if user.is_authenticated:
		return redirect('dashboard', email=request.user.email)
	return render(request, 'referral/home.html')

@login_required
def about(request):
	return render(request, 'referral/about.html')

@login_required
def dashboard(request, email):
	if request.user == User.objects.get(email=email):
		user = request.user
		user_bank = Bank.objects.filter(user=user)
		if user_bank.count() is 0:
			Bank.objects.create(user=user)
		else:
			if 'bank_info' in request.POST:
				b_form = BankUpdateForm(request.POST, instance=request.user.bank)
				if b_form.is_valid():
					bank = b_form.save(commit=False)
					bank.user = request.user
					bank.save()
					messages.success(request, f'Bank Details Updated')
					#send_mail('subject', 'body of the message', 'virazssolanki@gmail.com', [email])
					return redirect('dashboard', email=email)
			elif 'new_referral' in request.POST:
				r_form = NewReferral(request.POST)
				if r_form.is_valid():
					referral = r_form.save(commit=False)
					referral.reference = request.user
					name  = r_form.cleaned_data.get('name')
					referral.save()
					messages.success(request, f'Successfully referred : {name}')
					#send_mail('subject', 'body of the message', 'virazssolanki@gmail.com', [email])
					return redirect('dashboard', email=email)
		b_form = BankUpdateForm(instance=request.user.bank)
		r_form = NewReferral()
		referrals = Referrals.objects.filter(reference=user).order_by('-date_posted')
		success_referral = Referrals.objects.filter(reference=user).filter(status='success').order_by('-date_posted')
		pending_referral = Referrals.objects.filter(reference=user).filter(status='pending').order_by('-date_posted')
		withdraw_req = Withdraw.objects.filter(holder=user).order_by('-date_posted')
		bank_info = Bank.objects.get(user=user)
		total = 0
		for i in referrals:
			if i.status == 'success':
				total = total + i.amount

	context = locals()
	return render(request, 'referral/dashboard.html', context)

@login_required
def console(request):
	if request.user.is_superuser:
		users = User.objects.all()
		context = locals()
		return render(request, 'referral/console.html', context)
	else:
		messages.success(request, f'sorry you dont havecaccess')
		return render(request, 'referral/home.html')

@login_required
def withdraw(request):
	user = request.user
	Withdraw.objects.create(holder=user)
	messages.success(request, f'Withdraw request submitted. Our executive will contact you. ')
	return redirect('dashboard', email=user.email)