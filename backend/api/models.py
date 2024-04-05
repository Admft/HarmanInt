from django.db import models
from django.contrib.auth.models import User  # Import the User model from Django's authentication framework

# Define a Note model representing a note object
class Note(models.Model):
    title = models.CharField(max_length=100)  # Define a CharField for the note title
    content = models.TextField()  # Define a TextField for the note content
    created_at = models.DateTimeField(auto_now_add=True)  # Define a DateTimeField for the creation timestamp, set to auto_now_add to automatically set the current datetime when a new object is created
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")  # Define a ForeignKey relationship with the User model, specifying that if the related user is deleted, all associated notes should be deleted as well. Also, specify a related_name to access notes from a user object

    def __str__(self):  # Define a string representation of the note object
        return self.title  # Return the title of the note as its string representation
