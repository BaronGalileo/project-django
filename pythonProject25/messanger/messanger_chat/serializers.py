from  rest_framework import serializers

from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'type')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPage
        fields = ('name', 'foto')





