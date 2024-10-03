from django.urls import path
from .views import globalNotesList, globalNotesDetails, studentGlobalNote

urlpatterns = [
    path('notes/', globalNotesList, name='globalNotesList'),
    path('note/<int:note_id>', globalNotesDetails, name='globalNotesDetails'),
    path('student/<str:student_id>', studentGlobalNote, name='studentGlobalNote')
]