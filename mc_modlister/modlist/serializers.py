from rest_framework import serializers

from .models import TrackedMods

class TrackedModsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedMods
        fields = '__all__'