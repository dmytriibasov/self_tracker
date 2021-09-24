from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import ProcessFormView, BaseFormView

from .forms import CardForm, ReminderForm, GoalForm
from .models import Card, Goal, Reminder
from config import settings


# Create your views here.
class CardListView(LoginRequiredMixin, generic.ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'cards/list.html'
    login_url = settings.LOGIN_REDIRECT_URL

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


class CardDetailView(LoginRequiredMixin, generic.DetailView):
    model = Card
    pk_url_kwarg = 'card_pk'
    template_name = 'cards/detail.html'
    context_object_name = 'card'

    def dispatch(self, request, *args, **kwargs):
        card = self.get_object()
        if request.user.is_authenticated and card.user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse_lazy('common:home-page'))


class CardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Card
    pk_url_kwarg = 'card_pk'
    template_name = 'cards/delete.html'
    success_url = reverse_lazy('cards:list')

    def dispatch(self, request, *args, **kwargs):
        card = self.get_object()
        if request.user.is_authenticated and card.user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse_lazy('common:home-page'))


# REMINDER`s VIEWS
class CardReminderCreateView(LoginRequiredMixin, ProcessFormView):
    template_name = 'cards/new.html'
    card_form = CardForm
    reminder_form = ReminderForm
    title = 'Create page'

    def get(self, request, *args, **kwargs):
        context = {
            'card_form': self.card_form,
            'reminder_form': self.reminder_form,
            'title': self.title,
        }
        return render(request, self.template_name, context or {})

    def post(self, request, *args, **kwargs):

        card_form = self.card_form(request.POST)
        reminder_form = self.reminder_form(request.POST)
        context = {
            'card_form': self.card_form,
            'reminder_form': self.reminder_form,
        }

        if card_form.is_valid() and reminder_form.is_valid():

            # Card part
            card_form.instance.user = request.user
            card_form.save()

            # Reminder part
            reminder_form.instance.card = card_form.instance
            reminder_form.save()

            return HttpResponseRedirect(reverse('cards:list'))

        return render(request, self.template_name, context or {})


class CardReminderUpdateView(LoginRequiredMixin, BaseFormView):
    pk_url_kwarg = 'card_pk'
    template_name = 'cards/update.html'
    success_url = reverse_lazy('cards:list')

    def get(self, request, *args, **kwargs):

        # Card part
        card_pk = self.kwargs.get('card_pk')
        card = get_object_or_404(Card, pk=card_pk)
        card_form = CardForm(instance=card)

        # Reminder part
        reminder = get_object_or_404(Reminder, pk=card.reminders.id)
        reminder_form = ReminderForm(instance=reminder)
        context = {
            'card_form': card_form,
            'reminder_form': reminder_form,
        }
        return render(request, self.template_name, context or {})

    def post(self, request, *args, **kwargs):

        # Card part
        card_pk = self.kwargs.get('card_pk')
        card = get_object_or_404(Card, pk=card_pk)
        card_form = CardForm(instance=card)

        # Reminder part
        reminder = get_object_or_404(Reminder, pk=card.reminders.id)
        reminder_form = ReminderForm(instance=reminder)

        context = {
            'card_form': card_form,
            'reminder_form': reminder_form,
        }

        if card_form.is_valid and reminder_form.is_valid:

            # Card part
            card.title = self.request.POST.get('title')
            card.description = self.request.POST.get('description')
            card.evaluation = self.request.POST.get('evaluation')

            # Reminder part
            is_active = False
            if self.request.POST.get('is_active') == 'true':
                is_active = True

            reminder.comment = self.request.POST.get('comment')
            reminder.remind_time = self.request.POST.get('remind_time')
            reminder.is_active = is_active

            if card.user == request.user:
                card.save()
                reminder.save()
                return HttpResponseRedirect(reverse('cards:list'))

        return render(request, self.template_name, context or {})

    def dispatch(self, request, *args, **kwargs):
        card_pk = self.kwargs.get('card_pk')
        card = get_object_or_404(Card, pk=card_pk)
        if request.user.is_authenticated and card.user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse_lazy('common:home-page'))


# Goal`s Views
class GoalCreateView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    template_name = 'goals/new.html'
    fields = ('title', 'description', 'evaluation')
    context_object_name = 'goal'

    login_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.card = self.get_card()
        obj.save()
        return HttpResponseRedirect(obj.card.get_absolute_url())

    def get_card(self):
        return get_object_or_404(Card, id=self.kwargs.get('card_pk'))


class GoalEditView(LoginRequiredMixin, generic.UpdateView):

    model = Goal
    template_name = 'goals/detail.html'
    form_class = GoalForm
    pk_url_kwarg = 'goal_pk'
    context_object_name = 'goal'

    def get_success_url(self):
        return self.object.card.get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse_lazy('common:home-page'))


class GoalDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Goal
    pk_url_kwarg = 'goal_pk'
    template_name = 'goals/delete.html'

    def get_success_url(self):
        return self.object.card.get_absolute_url()
