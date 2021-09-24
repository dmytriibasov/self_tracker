from django.urls import path, include
from .views import (
    CardListView, CardReminderCreateView, CardDetailView, CardReminderUpdateView, CardDeleteView, GoalEditView,
    GoalCreateView, GoalDeleteView
)


app_name = 'cards'

goal_patterns = [
    path('', GoalCreateView.as_view(), name='goal-new'),
    path('<int:goal_pk>/', GoalEditView.as_view(), name='goal-detail'),
    # path('<int:goal_pk>/delete/', delete_goal, name='goal-delete'),
    path('<int:goal_pk>/delete/', GoalDeleteView.as_view(), name='goal-delete'),
]

urlpatterns = [
    path('', CardListView.as_view(), name='list'),
    path('new/', CardReminderCreateView.as_view(), name='new'),
    path('<int:card_pk>/', CardDetailView.as_view(), name='detail'),
    path('<int:card_pk>/update/', CardReminderUpdateView.as_view(), name='update'),
    path('<int:card_pk>/delete/', CardDeleteView.as_view(), name='delete'),
    path('<int:card_pk>/goal/', include(goal_patterns)),
    # path('<int:card_pk>/goal/<int:goal_pk>/', GoalEditView.as_view(), name='goal-detail'),
    # path('<int:card_pk>/goal/<int:goal_pk>/delete/', GoalDeleteView.as_view(), name='goal-delete'),
    # path('<int:card_pk>/goal/<int:goal_pk>', GoalDeleteView.as_view(), name='goal-delete'), ### ???
    # path('<int:card_pk>/update/', CardUpdateView.as_view(), name='update'),
    # path('new/', cardCreateView.as_view(), name='new'),
]
