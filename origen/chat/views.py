from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied
from . import serializers
from . import models

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class EditSessionView(viewsets.ViewSet):
    serializer_class = serializers.SessionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.EditSession.objects.filter(user=user)

class EditSessionAllowedView(viewsets.ViewSet):
    serializer_class = serializers.SessionAllowedSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.EditSessionAllowed.objects.filter(user=user)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        session_id = serializer.data['session_id']
        requested_user = serializer.data['user']
        user = request.user
        sessions = EditSession.all().filter(user=user, session_id=session_id)
        if sessions.count == 0:
            raise PermissionDenied({"message":"You don't have permission to access"})
        adder = models.EditSessionAllowed(session_id=session_id, user=requested_user)
        adder.save()
