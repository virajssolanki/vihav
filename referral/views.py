from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User, Bank, Profile
from .models import Referrals, Withdraw
from users.forms import BankUpdateForm, NewReferral, NewAdminReferral, UpdateReferral, UpdateWithdraw
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='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'

def home(request):
	user=request.user
	if user.is_authenticated:
		return redirect('dashboard', email=request.user.email)
	else:
		return redirect('signup')
	return render(request, 'referral/home.html')

@login_required
def about(request):
	return render(request, 'referral/newabout.html')

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
def console(request, rpk=None, wpk=None):
	if request.user.is_superuser:
		user = request.user
		if request.method == 'POST':
			r_form = NewAdminReferral(request.POST)
			if r_form.is_valid():
				ref_email = r_form.cleaned_data.get('reference_email')
				ref = User.objects.get(email=ref_email)
				name  = r_form.cleaned_data.get('name')
				referral = r_form.save(commit=False)
				referral.reference = ref
				referral.save()
				messages.success(request, f'Referral {name} Added with reference {ref_email}')
				#message = Mail(
					#from_email='vihavgroup.dm@gmail.com',
					#to_emails=ref_email,
					#subject=f'{name} book property at vihav with your reference',
					#html_content='<h1>Welcome to Vihav Privilege</h1><strong>and easy to do anywhere, even with Python</strong>')
				#sg = SendGridAPIClient(SENDGRID_API_KEY)
				response = sg.send(message)
		if rpk != None and wpk==None:
			ref = Referrals.objects.get(id=rpk)
			if request.method == 'POST':
				urform = UpdateReferral(request.POST, instance=ref)
				if urform.is_valid:
					ref = urform.save(commit=False)
					status  = urform.cleaned_data.get('status')
					lert = alert(status)
					ref.alert = lert
					ref.save()
					messages.success(request, f'REFERRAL UPDATED SUCCESSFULLY')
					return redirect('console')
			else:
				urform = UpdateReferral(instance=ref)

		if wpk != None and rpk==None:
			w = Withdraw.objects.get(id=wpk)
			if request.method == 'POST':
				wd_form = UpdateWithdraw(request.POST, instance=w)
				if wd_form.is_valid:
					w = wd_form.save(commit=False)
					status  = wd_form.cleaned_data.get('status')
					lert = alert(status)
					w.alert = lert
					w.save()
					messages.success(request, f'Withdraw request updated')
					return redirect('console')
			else:
				wd_form = UpdateWithdraw(instance=w)

		r_form = NewAdminReferral()
		acc_req = Profile.objects.filter(verified=False).order_by('-date_posted')
		ref_req = Referrals.objects.order_by('-date_posted')
		wd_req = Withdraw.objects.order_by('-date_posted')
		context = locals()
		return render(request, 'referral/console.html', context)
	else:
		return render(request, 'referral/home.html')

@login_required
def all_req(request):
	if request.user.is_superuser:
		user = request.user
		acc_req = Profile.objects.filter(verified=False).order_by('-date_posted')
		context = locals()
		return render(request, 'referral/all_req.html', context)
	else:
		return render(request, 'referral/home.html')

@login_required
def all_ref(request):
	if request.user.is_superuser:
		user = request.user
		if request.method == 'POST':
			r_form = NewAdminReferral(request.POST)
			if r_form.is_valid():
				ref_email = r_form.cleaned_data.get('reference_email')
				ref = User.objects.get(email=ref_email)
				name  = r_form.cleaned_data.get('name')
				referral = r_form.save(commit=False)
				referral.reference = ref
				referral.save()
				messages.success(request, f'Referral {name} Added with reference {ref_email}')
		r_form = NewAdminReferral()
		ref_req = Referrals.objects.order_by('-date_posted')
		context = locals()
		return render(request, 'referral/all_ref.html', context)
	else:
		return render(request, 'referral/home.html')

@login_required
def accept(request, pk):
	if request.user.is_superuser:
		acc = Profile.objects.get(id=pk)
		acc.verified = True
		acc.is_client = True
		acc.save()
		email = acc.user.email
		messages.success(request, f'Account created')
		#message = Mail(
		#	from_email='vihavgroup.dm@gmail.com',
		#	to_emails=email)
		#message.template_id = 'd-9cbebf3c4241460fbcac2b6c4d378d4b'
		#sg = SendGridAPIClient(SENDGRID_API_KEY)
		#response = sg.send(message)
		return redirect('console')
	else:
		return render(request, 'referral/home.html')

@login_required
def delete(request, pk):
	if request.user.is_superuser:
		acc = Profile.objects.get(id=pk)
		acc.verified = True
		acc.is_client = False
		acc.save()
		messages.success(request, f'Account rejected')
		return redirect('console')
	else:
		return render(request, 'referral/home.html')

def alert(status):
	if status == 'success':
		alert = 'success'
	elif status == 'pending':
		alert = 'warning'
	elif status == 'fail':
		alert = 'danger'
	return alert

@login_required
def edit_ref(request, pk):
	if request.user.is_superuser:
		ref = Referrals.objects.get(id=pk)
		if request.method == 'POST':
			urform = UpdateReferral(request.POST, instance=ref)
			if urform.is_valid:
				ref = urform.save(commit=False)
				status  = urform.cleaned_data.get('status')
				lert = alert(status)
				ref.alert = lert
				ref.save()
				messages.success(request, f'REFERRAL UPDATED SUCCESSFULLY')
				return redirect('console')
		else:
			urform = UpdateReferral(instance=ref)
		context = locals()
		return render(request, 'referral/console.html', context)
	else:
		return render(request, 'referral/home.html')



@login_required
def withdraw(request):
	user = request.user
	Withdraw.objects.create(holder=user)
	messages.success(request, f'Withdraw request submitted. Our executive will contact you. ')
	return redirect('dashboard', email=user.email)

