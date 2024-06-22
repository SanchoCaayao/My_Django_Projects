# urls.py     URL for the notes

from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # URL pattern for listing all notes
    path('note/<int:pk>/', views.note_detail, name='note_detail'),  # URL pattern for viewing a single note
    path('note/new/', views.note_create, name='note_create'),  # URL pattern for creating a new note
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),  # URL pattern for updating an existing note
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),  # URL pattern for deleting a note
]
