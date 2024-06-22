# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# The view for listing all notes.
def note_list(request):
    notes = Note.objects.all()  # Retrieve all notes from the database.
    # Render the note list template with the notes.
    return render(request, 'notes/note_list.html', {'notes': notes})  

# The view for displaying a single note.
def note_detail(request, pk):
    # Retrieve the note with the specified primary key, or return a 404 error if not found.
    note = get_object_or_404(Note, pk=pk)  
    # Render the note detail template with the note.
    return render(request, 'notes/note_detail.html', {'note': note})  

# The view for creating a new note.
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)  # Bind the form with POST data.
        if form.is_valid():
            form.save()  # Save the new note to the database.
            return redirect('note_list')  # Redirect to the note list view.
    else:
        form = NoteForm()  # Create an empty form instance.
    # Render the note form template with the form.
    return render(request, 'notes/note_form.html', {'form': form})  

# The view for updating an existing note.
def note_update(request, pk):
    # Retrieve the note with the specified primary key.
    # Or return a 404 error if not found.
    note = get_object_or_404(Note, pk=pk)  
    if request.method == 'POST':
        # Bind the form with POST data and the existing note instance.
        form = NoteForm(request.POST, instance=note)  
        if form.is_valid():
            form.save()  # Save the updated note to the database.
            return redirect('note_list')  # Redirect to the note list view.
    else:
        form = NoteForm(instance=note)  # Create a form instance with the existing note data.
        # Render the note form template with the form.
    return render(request, 'notes/note_form.html', {'form': form})  

# The view for deleting an existing note.
def note_delete(request, pk):
    # Retrieve the note with the specified primary key.
    # Or return a 404 error if not found.
    note = get_object_or_404(Note, pk=pk)  
    if request.method == 'POST':
        note.delete()  # Delete the note from the database.
        return redirect('note_list')  # Redirect to the note list view.
     # Render the note delete confirmation template with the note.
    return render(request, 'notes/note_confirm_delete.html', {'note': note}) 
