from django.db import models
from django.contrib.auth.models import User


class Spot(models.Model):
    SPOT_TYPES = (
        ('beach', 'Beach'),
        ('lake', 'Lakes'),
        ('river', 'Rivers'),
        ('waterfall', 'Waterfalls'),
        ('pool', 'Pools'),
        ('cave', 'Caves'),
        # ... any other types
    )

    name = models.CharField(max_length=255)
    spot_type = models.CharField(max_length=50, choices=SPOT_TYPES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    images = models.ImageField(upload_to='spots/', blank=True, null=True)  # Assuming you're using ImageField
    safety_information = models.OneToOneField('SafetyInformation', on_delete=models.CASCADE, null=True)
    regulations = models.OneToOneField('Regulation', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class SafetyInformation(models.Model):
    details = models.TextField()
    water_quality = models.CharField(max_length=255, blank=True, null=True)
    currents = models.CharField(max_length=255, blank=True, null=True)

    # ... any other fields you deem necessary

    def __str__(self):
        return f"Safety Information for {self.spot.name}"


class Regulation(models.Model):
    details = models.TextField()
    protected_areas = models.CharField(max_length=255, blank=True, null=True)
    seasonal_restrictions = models.TextField(blank=True, null=True)
    required_permits = models.TextField(blank=True, null=True)

    # ... any other fields you deem necessary

    def __str__(self):
        return f"Regulations for {self.spot.name}"


class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} checked-in at {self.spot.name}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} favorited {self.spot.name}"
