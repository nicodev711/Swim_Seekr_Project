from django.urls import path
from . import views

urlpatterns = [
    path('spots/', views.SpotListCreateView.as_view(), name='spot-list-create'),
    path('spots/<int:pk>/', views.SpotRetrieveUpdateDestroyView.as_view(), name='spot-detail'),

    path('checkins/', views.CheckInListCreateView.as_view(), name='checkin-list-create'),
    path('checkins/<int:pk>/', views.CheckInRetrieveUpdateDestroyView.as_view(), name='checkin-detail'),

    path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', views.FavoriteRetrieveUpdateDestroyView.as_view(), name='favorite-detail'),
]
