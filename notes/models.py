
# Create your models here.

from django.db import models

# The Note model represents a sticky note with a title, content, and a timestamp for when it was created.
class Note(models.Model):
    title = models.CharField(max_length=100)  # The title of the note, limited to 100 characters.
    content = models.TextField()  # The content of the note.
    created_at = models.DateTimeField(auto_now_add=True)  # The timestamp for when the note was created, automatically set when the note is first created.

    def __str__(self):
        return self.title  # Returns the title of the note when the object is printed.
