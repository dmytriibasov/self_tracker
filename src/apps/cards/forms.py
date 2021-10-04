from django import forms
from .models import Card, Goal, Reminder
from django.utils import timezone


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'description', )


class ReminderForm(forms.ModelForm):

    class Meta:
        model = Reminder
        fields = ('comment', 'is_active', 'remind_time',)


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ('title', 'description', )


class RatingForm(forms.Form):

    value = forms.IntegerField(max_value=10, min_value=0)

