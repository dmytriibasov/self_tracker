from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    WelcomePageView, HomePageView, ChangePasswordView, PasswordChangeDoneView, PasswordResetCustomView,
    PasswordResetDoneCustomView, PasswordResetConfirmCustomView, PasswordResetCompleteCustomView,
                    )

app_name = 'common'

urlpatterns = [

    # Common URL`s
    path('', WelcomePageView.as_view(), name='welcome-page'),
    path('home/', HomePageView.as_view(), name='home-page'),


    # Auth URL`s
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout-page'),


    # Password change & reset URL`s
    path('user/change_password/', ChangePasswordView.as_view(), name='password-change-page'),
    path('user/change_password/done', PasswordChangeDoneView.as_view(), name='password-change-done-page'),

    path('password_reset/', PasswordResetCustomView.as_view(), name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneCustomView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmCustomView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteCustomView.as_view(),
         name='password_reset_complete'),
]