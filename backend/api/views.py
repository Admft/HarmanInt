from django.shortcuts import render  # Import render function from Django
from django.contrib.auth.models import User  # Import the User model from Django's authentication framework
from rest_framework import generics  # Import generics module from Django REST Framework
from .serializers import UserSerializer, NoteSerializer  # Import UserSerializer and NoteSerializer from local serializers module
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import IsAuthenticated and AllowAny permission classes from Django REST Framework
from .models import Note  # Import the Note model from the local models module

# View for listing and creating notes
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer  # Specify the serializer class to be used
    permission_classes = [IsAuthenticated]  # Specify the permission classes required for this view

    # Method to get the queryset for the view
    def get_queryset(self):
        user = self.request.user  # Get the current user from the request
        return Note.objects.filter(author=user)  # Return queryset filtered by the current user's notes

    # Method to perform creation of a new note
    def perform_create(self, serializer):
        if serializer.is_valid():  # Check if the serializer is valid
            serializer.save(author=self.request.user)  # Save the note with the current user as the author
        else:
            print(serializer.errors)  # Print serializer errors if validation fails

# View for deleting a note
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer  # Specify the serializer class to be used
    permission_classes = [IsAuthenticated]  # Specify the permission classes required for this view

    # Method to get the queryset for the view
    def get_queryset(self):
        user = self.request.user  # Get the current user from the request
        return Note.objects.filter(author=user)  # Return queryset filtered by the current user's notes

# View for creating a new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Specify the queryset for the view
    serializer_class = UserSerializer  # Specify the serializer class to be used
    permission_classes = [AllowAny]  # Specify the permission classes required for this view
