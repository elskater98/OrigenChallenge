from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from . import serializers
from . import models

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class EditSessionView(viewsets.ModelViewSet):
    serializer_class = serializers.SessionSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        owner = models.EditSession.objects.filter(user=user)
        # added = models.EditSessionAllowed.objects.filter(user=user).values_list('__session', flat=True)
        # print('\n'*50)
        # print(added)
        return owner
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.data['name']
        user = request.user
        models.EditSession.objects.create(name=name, user=user)
        return Response({"status": "Success"})  

class EditSessionAllowedView(viewsets.ModelViewSet):
    serializer_class = serializers.SessionAllowedSerializer
    permission_classes = (AllowAny, )

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

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )