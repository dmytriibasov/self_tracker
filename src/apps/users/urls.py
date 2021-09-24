from django.urls import path

from .views import UserRegisterView, UserProfileView, UserDeleteView

app_name = 'users'

urlpatterns = [

    # User profile URL`s
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('<int:user_pk>/profile/', UserProfileView.as_view(), name='profile-page'),
    path('<int:user_pk>/profile/delete/', UserDeleteView.as_view(), name='delete-page'),

]