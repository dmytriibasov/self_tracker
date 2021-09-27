from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from .models import Reminder
from django.utils import timezone


@shared_task()
def send_email():
    reminders_qs = Reminder.objects.all().is_active()
    for reminder in reminders_qs:

        email = EmailMessage(
            subject=f'Hello {reminder.card.user}',
            body=f'Did you track your progress today? Remind_time = {reminder.remind_time}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[reminder.card.user.email]
        )
        if reminder.remind_time.strftime("%H:%M") == timezone.localtime().strftime("%H:%M"):
            email.send()
