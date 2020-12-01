from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'name')


class OpeningMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningMessage
        fields = ["id", "owner", "message"]


class UserProfileSerializer(serializers.ModelSerializer):
    interests = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = ['bio', 'birthday', 'avatar', 'interests']


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
        fields = ['id', 'source', 'target', 'opening_message', 'state', 'message']
