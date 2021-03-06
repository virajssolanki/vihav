from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Profile
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='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'

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
				name  = form.cleaned_data.get('first_name')
				last_name  = form.cleaned_data.get('last_name')
				city  = form.cleaned_data.get('adress')
				number  = form.cleaned_data.get('contact_number')
				i_am  = form.cleaned_data.get('i_am')
				site  = form.cleaned_data.get('sites')
				Profile.objects.create(user=user, name=name, last_name=last_name, city=city, number=number, i_am=i_am, site=site)
				login(request, user)
				message = Mail(
					from_email='one@vihav.com',
					to_emails=email)
				message.template_id = 'd-581e4afb46eb4ee08bfa2eb11128474b'
				sg = SendGridAPIClient(SENDGRID_API_KEY)
				response = sg.send(message)

				message = Mail(
					from_email='one@vihav.com',
					to_emails='one@vihav.com')
				message.template_id = 'd-06939b7504624457bf3fbc78b6b449c0'
				message.dynamic_template_data = {
						'name': name,
						'last_name': last_name,
						'email': email,
						'number': number,
						'address': city,
						'relation': i_am,
						'site': site,
							}
				sg = SendGridAPIClient(SENDGRID_API_KEY)
				response = sg.send(message)			
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
