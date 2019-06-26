from rest_framework import serializers
from .models import Songs,EntryValues


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryValues
        fields = ("script", "language","versionIndex")


