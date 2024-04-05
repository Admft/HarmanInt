from django.contrib.auth.models import User  # Import the User model from Django's authentication framework
from rest_framework import serializers  # Import serializers module from Django REST Framework
from .models import Note  # Import the Note model from the local models module

# Define a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serializer
    class Meta:
        model = User  # Specify the User model
        # Define the fields to be included in the serialized representation
        fields = ["id", "username", "password"]
        # Specify extra keyword arguments for certain fields
        extra_kwargs = {
            "password": {"write_only": True}  # Password should only be written, not displayed
        }
    
    # Define a custom create method to handle user creation
    def create(self, validated_data):
        # Use the User manager's create_user method to create a new user with the validated data
        user = User.objects.create_user(**validated_data)
        return user

# Define a serializer for the Note model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # Specify the Note model
        # Define the fields to be included in the serialized representation
        fields = ["id", "title", "content", "created_at", "author"]
        # Specify extra keyword arguments for certain fields
        extra_kwargs = {"author": {"read_only": True}}  # Author field should be read-only
