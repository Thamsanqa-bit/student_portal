from django.shortcuts import render
from .serializers import DashboardSerializer

from dashboard.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def notes_list(request):
    notes = Notes.objects.all()
    serializer = DashboardSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def notesCreate(request):
    serializer = DashboardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def notesUpdate(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = DashboardSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def notesDelete(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()

    return Response('Item Successfully Deleted!!')

