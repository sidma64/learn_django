from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import parser_classes
from django.contrib.auth.models import User
from . import models
from rest_framework.parsers import JSONParser
import io

class UserList(APIView):
    """
    View to list all users in the system.
    """

    parser_classes = [JSONParser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    
    def post(self, request, format=None):
        """
        Create a new user.
        """
        serializer = models.UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({'error': 'Please provide both username and password'},
                            status=400)
        user = serializer.save()
        return Response({'username': user.username}, status=201)
