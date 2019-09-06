from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=240)
    venue = serializers.CharField(max_length=60)
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    # creator = serializers.StringRelatedField()
    # attendee = serializers.StringRelatedField(many=True)