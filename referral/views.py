from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Referrals
# Create your views here.
def home(request):
	user=request.user
	if user.is_authenticated:
		return redirect('dashboard', email=request.user.email)
	return render(request, 'referral/home.html')

@login_required
def dashboard(request, email):
	if request.user == User.objects.get(email=email):
		user = request.user
		referrals = Referrals.objects.filter(reference=user).order_by('date_posted')
		success_referral = Referrals.objects.filter(reference=user).filter(status='success').order_by('date_posted')
		pending_referral = Referrals.objects.filter(reference=user).filter(status='pending').order_by('date_posted')
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
		messages.success(request, f'sorry you dont haveacces')
		return render(request, 'referral/home.html')

