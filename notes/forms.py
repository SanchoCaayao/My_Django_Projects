# forms.py 

from django import forms
from .models import Note

# The form for creating and updating notes.
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note  # Specify the model that the form is based on.
        fields = ['title', 'content']  # Specify the fields to include in the form.
