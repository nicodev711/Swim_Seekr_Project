from django.urls import path
from .views import (
    UserProfileListCreateView, UserProfileDetailView,
    UserPreferencesListCreateView, UserPreferencesDetailView
)

urlpatterns = [
    path('users/', UserProfileListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='user-detail'),
    path('users/preferences/', UserPreferencesListCreateView.as_view(), name='preferences-list-create'),
    path('users/preferences/<int:pk>/', UserPreferencesDetailView.as_view(), name='preferences-detail'),
]
