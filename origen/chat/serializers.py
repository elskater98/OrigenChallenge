from rest_framework import serializers
from . import models

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EditSession
        fields = ['session_id']

class SessionAllowedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EditSessionAllowed
        fields = ['session_id', 'user']