from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Room
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@api_view(['POST'])
def book_room(request):
    if request.method=="POST":
         room_number=request.data.get('room_number')
         try:
             room=Room.objects.get(room_number=room_number)
             if room.available:
                 room.available=False
                 room.save()
                 serializer=RoomSerializer(room)
                 response_data={
                     'msg':'Room Booked sucessfully',
                     'room':serializer.data,
                 }
                 return Response(response_data)
             else:
                return Response(response_data={'msg':'Room not available'})
         except Room.DoesNotExist:
                return Response({"message":"Room is not found"})
@api_view(['GET'])
def test_api(request):
     room=Room.objects.all()
     serializer=RoomSerializer(room,many=True)
     return Response(serializer.data)   
@api_view(['GET'])
def check_availability(request,room_number):
     try:
          room=Room.objects.get(room_number=room_number)
          serializer=RoomSerializer(room)
          return Response(serializer.data)
     except Room.DoesNotExist:
          return Response({'msg':'Room not found'})        
        
'''
def room_availability(request,id):
    if request.method=="POST":
        room=Room.objects.get(pk=id)
        serializer=RoomSerializer(room)
        if room.available=='false':
            data={'available':room.available}
            return JsonResponse(data)
'''
'''
class Room_api(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    
'''
