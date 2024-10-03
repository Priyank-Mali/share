from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import globalNote
from .serializers import globalNoteSerializers

@api_view(['GET', 'POST'])
def  globalNotesList(request):
    if request.method == 'POST':
        serializer = globalNoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'GET':
        querySet = globalNote.objects.all()
        print(querySet)
        serializer = globalNoteSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def  globalNotesDetails(request, note_id):
    try:
        querySet = globalNote.objects.get(id=note_id)
    except globalNote.DoesNotExist:
        data = {
            'message' : "Note not found"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = globalNoteSerializers(querySet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = globalNoteSerializers(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = globalNoteSerializers(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data = {
            'message':f'Note-ID : {note_id} is deleted successfully.'
        }
        querySet.delete()
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def studentGlobalNote(request, student_id):
    querySet = globalNote.objects.filter(student_id=student_id)
    if not querySet.exists():
        data = {
            'message': "Note not found"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = globalNoteSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)