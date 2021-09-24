from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import UserRegisterForm, UserUpdateForm
from .models import CardUser


# User CRUD View`s
class UserRegisterView(generic.CreateView):
    model = CardUser
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    context_object_name = 'form'
    success_url = reverse_lazy(viewname='common:login-page')


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    model = CardUser
    pk_url_kwarg = 'user_pk'
    form_class = UserUpdateForm
    template_name = 'users/profile.html'
    context_object_name = 'form'
    success_url = reverse_lazy(viewname='common:home-page')

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_authenticated and user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse('common:welcome-page'))


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CardUser
    pk_url_kwarg = 'user_pk'
    template_name = 'users/delete.html'
    success_url = reverse_lazy(viewname='common:welcome-page')

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_authenticated and user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse_lazy('common:welcome-page'))
