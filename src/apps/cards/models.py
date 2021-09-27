from django.db import models
from config import settings
from django.utils import timezone

# Create your models here.
class Card(models.Model):

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cards',
    )

    title = models.CharField(
        max_length=100,
        blank=False,
    )

    description = models.TextField(
        max_length=255,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    evaluation = models.IntegerField()

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return f'Card name: {self.title}. Username: {self.user}'

    def get_absolute_url(self):
        return f'/cards/{self.id}/'


# Goals
class Goal(models.Model):

    card = models.ForeignKey(
        to=Card,
        on_delete=models.CASCADE,
        related_name='goals',
    )

    title = models.CharField(
        max_length=50,
        blank=False,
    )

    description = models.TextField(
        max_length=255,
    )

    evaluation = models.IntegerField(
        default=1,
        null=False,
    )

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def get_absolute_url(self):
        return f'/cards/{self.card.id}/goal/{self.id}/'

    def get_delete_url(self):
        return f'/cards/{self.card.id}/goal/{self.id}/delete/'

    def __str__(self):
        return f'{self.title}: description:{self.description} at {self.evaluation}'


# Reminders
class ReminderQuerySet(models.QuerySet):

    def is_active(self):
        return self.filter(is_active=True)


class Reminder(models.Model):
    card = models.OneToOneField(
        to=Card,
        on_delete=models.CASCADE,
        related_name='reminders'
    )

    is_active = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    remind_time = models.TimeField(
        default='21:00',
        null=True,
        blank=True,
    )

    remind_date = models.DateField(
        auto_now_add=True,
    )

    comment = models.TextField(
        max_length=255,
        blank=True,
        default='Add comment here'
    )

    created_at = models.DateTimeField(
        auto_now=True,
    )

    objects = ReminderQuerySet.as_manager()

    class Meta:
        verbose_name = "Reminder"
        verbose_name_plural = "Reminders"

    def __str__(self):
        return f'{self.comment}: status:{self.is_active} at {self.remind_time}'
