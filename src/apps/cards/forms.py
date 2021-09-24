from django import forms
from .models import Card, Goal, Reminder


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'description', 'evaluation')


class ReminderForm(forms.ModelForm):

    class Meta:
        model = Reminder
        fields = ('comment', 'is_active', 'remind_time',)


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ('title', 'description', 'evaluation', )
