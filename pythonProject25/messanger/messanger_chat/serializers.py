from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPage
        fields = ('name', 'foto')

    def create(self, validated_data):
        user = UserPage(
            name=validated_data['name'],
            foto=validated_data['foto']
        )

        user.save()
        return user

class MessageSerializer(serializers.ModelSerializer):
    date_formatted = serializers.SerializerMethodField()
    author = ProfileSerializer()

    class Meta:
        model = Message
        exclude = []
        depth = 1

    def get_date_formatted(self, obj: Message):
        return obj.date.strftime("%d-%m-%Y %H:%M:%S")


class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('pk', 'name', 'host', 'messages', "users", "last_message")
        depth = 1
        read_only_fields = ["messages", "last_message"]

    def get_last_message(self, obj: Room):
        return MessageSerializer(obj.messages.order_by('date').last()).data




