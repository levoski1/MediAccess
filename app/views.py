from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from typing import List, Tuple, Dict


# Mail
def send_gmail(*mail: Tuple) -> str:
    subject, message_body, user_email, user_name, phone = mail

     # Construct the email message
    message = f"Hello Admin,\n\nYou've received a new message from the contact form on your website.\n\n"
    message += f"Name: {user_name}\nEmail: {user_email}\nPhone: {phone}\nSubject: {subject}\n\nMessage:\n{message_body}\n\n"
    message += "Please reply directly to this email to contact the user."

    return message
    

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def contact(request):
    if request.method == 'POST':
        data = request.POST

        user_name = data.get('name')
        user_email = data.get('email')
        subject = data.get('subject')
        phone = data.get('phone')
        message_body = data.get('message')
        mail = send_gmail(subject, message_body, user_email, user_name, phone  )

        send_mail(subject=subject, message=mail, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=settings.ADMIN_EMAIL.split('_'), fail_silently=False)

        context = {
            'user_name': user_name,   
        }
        return render(request, 'app/contact.html', context)
    return render(request, 'app/contact.html')