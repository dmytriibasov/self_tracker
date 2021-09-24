from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext_lazy as _
from apps.users.models import CardUser


# Homepage View`s
class HomePageView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(to=reverse('common:welcome-page'))


# Welcome page view
class WelcomePageView(generic.TemplateView):
    template_name = 'welcome.html'


# Password Change View`s
class ChangePasswordView(auth_views.PasswordChangeView):
    model = CardUser
    form_class = PasswordChangeForm
    template_name = 'registration/password/password_change.html'
    success_url = reverse_lazy('common:password-change-done-page')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/password/password_changed_done.html'
    title = _('Password change successful')


# Password Reset View`s
class PasswordResetCustomView(auth_views.PasswordResetView):
    success_url = reverse_lazy('common:password_reset_done')
    email_template_name = 'registration/password/password_reset_email.html'
    subject_template_name = 'registration/password/password_reset_subject.txt'
    template_name = 'registration/password/password_reset_form.html'


class PasswordResetDoneCustomView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password/password_reset_done.html'
    pass


class PasswordResetCompleteCustomView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password/password_reset_complete.html'
    pass


class PasswordResetConfirmCustomView(auth_views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('common:password_reset_complete')
    template_name = 'registration/password/password_reset_confirm.html'
