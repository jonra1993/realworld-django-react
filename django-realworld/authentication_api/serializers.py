from django.contrib.auth import authenticate
from django.contrib.auth import authenticate

from rest_framework import serializers

#from conduit.apps.profiles.serializers import ProfileSerializer
from authentication_api.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)

