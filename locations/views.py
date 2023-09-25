from rest_framework import generics
from .models import *
from .serializers import *


# Spot Views
class SpotListCreateView(generics.ListCreateAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class SpotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


# CheckIn Views
class CheckInListCreateView(generics.ListCreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class CheckInRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


# Favorite Views
class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class FavoriteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
