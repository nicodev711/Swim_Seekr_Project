from rest_framework import serializers
from .models import Spot, SafetyInformation, Regulation, CheckIn, Favorite


class SafetyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyInformation
        fields = '__all__'


class RegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regulation
        fields = '__all__'


class SpotSerializer(serializers.ModelSerializer):
    safety_information = SafetyInformationSerializer()
    regulations = RegulationSerializer()

    class Meta:
        model = Spot
        fields = '__all__'


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
