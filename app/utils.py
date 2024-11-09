from typing import Tuple, Dict


# Mail
def from_contact(*mail: Tuple) -> str:
    '''
    This functiion 5 arguments and they are passed accordinly.
    '''
    subject, message_body, user_email, user_name, phone = mail

     # Construct the email message
    message = f"Hello Admin,\n\nYou've received a new message from the contact form on your website.\n\n"
    message += f"Name: {user_name}\nEmail: {user_email}\nPhone: {phone}\nSubject: {subject}\n\nMessage:\n{message_body}\n\n"
    message += "Please reply directly to this email to contact the user."

    return message

def from_book(*mail: Tuple) -> str:
    '''
    This functiion 5 arguments and they are passed accordinly.
    '''
    subject, message_body, user_email, user_name, date = mail

     # Construct the email message
    message = f"Hello Admin,\n\nYou've received a new message from the contact form on your website.\n\n"
    message += f"Name: {user_name}\nEmail: {user_email}\nAppointment Date: {date}\nSubject: {subject}\n\nMessage:\n{message_body}\n\n"
    message += "Please reply directly to this email to contact the user."

    return message