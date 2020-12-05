from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import threading
import sendgrid
import time
from sendgrid.helpers.mail import Mail
from .models import Email


def create_data(text, date):
    """
    Подготовка данных для шаблона в Sendgrid
    """
    data = {
       "data": {
          "sent_datetime": "UTC " + date.strftime("%c"),
          "text": text
       }
    }
    return data


def send_email(to_email, template_data):
    """
    Непосредственно отправка сообщения через Sendgrid
    """
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    message = Mail(
            from_email=settings.SENDGRID_FROM,
            to_emails=to_email,
    )
    message.template_id = settings.SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    response = sg.send(message)
    return response


def schedule_email(em):
    """
    Берем в работу отправку email
    """
    em.status = Email.STATUS_SHCEDULED
    em.save()
    time.sleep(em.delay)
    em.status = Email.STATUS_SENT
    try:
        resp = send_email(em.to_email,
                create_data(em.body_text, em.scheduled_for))
    except Exception as e:
        em.status = Email.STATUS_SENT_ERROR
    em.save()



@receiver(post_save, sender=Email)
def email_added(sender, instance, created, **kwargs):
    """
    Обрабатываем сигнал добавления Email
    """
    if created:
        t = threading.Thread(target=schedule_email, args=(instance, ))
        t.start()
