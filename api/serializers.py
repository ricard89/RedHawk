from main_app.models import Tag
from rest_framework import serializers
#from django.contrib.auth.models import User
from accounts.models import User


class TagSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tag
        fields = ('owner', 'id', 'num_ID', 'name_ID', 'device', 'value', 'unit', 'type', 'widget', 'arguments')
        # read_only_fields = ()


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'email', 'device_token')
