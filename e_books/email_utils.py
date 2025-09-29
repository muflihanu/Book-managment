from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(user_email, username):
    """Send welcome email when user registers"""
    subject = 'Welcome to Book Management System! 📚'
    message = f"""
    Dear {username},

    Welcome to Book Management System! Your account has been successfully created.

    With your account, you can:
    • View all your books in one place
    • Update book information
     We're excited to help you organize your reading journey!
     """

    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False