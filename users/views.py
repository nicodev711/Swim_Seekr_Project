from rest_framework import generics
from .models import UserProfile, UserPreferences
from .serializers import UserProfileSerializer, UserPreferencesSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserPreferencesListCreateView(generics.ListCreateAPIView):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer


class UserPreferencesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer
