from django.contrib.auth.models import User, Group
from rest_framework import serializers
from octavius.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Sleep


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SleepSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sleep = serializers.CharField(required=False, allow_null=True, default=None)
    wakeup = serializers.CharField(required=False, allow_null=True, default=None)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Sleep.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.sleep = validated_data.get('sleep', instance.sleep)
        instance.wakeup = validated_data.get('code', instance.wakeup)
        instance.save()
        return instance