from celery import shared_task
from time import sleep
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='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'

def alert(status):
	if status == 'success':
		alert = 'success'
	elif status == 'pending':
		alert = 'warning'
	elif status == 'fail':
		alert = 'danger'
	return alert

@shared_task
def sleepy(duration):
	sleep(duration)
	return None

@shared_task
def send_email():
	message = Mail(
		from_email='one@vihav.com',
		to_emails='team.gilool@gmail.com',
		subject=f'with celery',
		html_content='<h1>Welcome to Vihav Privilege</h1><strong>and easy to do anywhere, even with Python</strong>')
	sg = SendGridAPIClient(SENDGRID_API_KEY)
	response = sg.send(message)
	return None