from rest_framework import serializers

from .models import Modlist

class ModlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modlist
        fields = [
            'mod_id',
            'name',
            'installed_version',
            'modloader',
            'mc_version',
            'last_updated',
        ]