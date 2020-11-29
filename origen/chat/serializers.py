from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditSession
        fields = ['session_id', 'name', 'date_created']

class SessionAllowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EditSessionAllowed
        fields = ['session', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user