from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class OpeningMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningMessage
        fields = ["id", "owner", "message"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birthday', 'avatar', 'interests', 'requests']


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['subject']


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['name']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = ['req_from', 'req_to', 'req_opening_message', 'req_state']
