from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Profile
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.core.mail import send_mail

def signup(request):
	user=request.user
	if not user.is_authenticated:
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				email  = form.cleaned_data.get('email')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(email=email, password=raw_password)
				name  = form.cleaned_data.get('name')
				city  = form.cleaned_data.get('city')
				number  = form.cleaned_data.get('number')
				Profile.objects.create(user=user, name=name, city=city, number=number)
				login(request, user)
				messages.success(request, f'ACCOUNT CREATED FOR {email}!')
				send_mail('subject', 'body of the message', 'virazssolanki@gmail.com', [email])
				return redirect('dashboard', email=email)
		else:
			form = UserRegisterForm()
		context = locals()
		return render(request, 'users/signup.html', context)
	else:
		return redirect('home') 

@login_required
def updateprofile(request, email):
	user = User.objects.get(email=email)
	if request.user == user:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f'PROFILE UPDATED SUCCESSFULLY')
				return redirect('referral/home')
		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.profile)
	context = locals()
	return render(request, 'users/updateprofile.html', context)
