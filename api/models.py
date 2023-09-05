from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


# Create your models here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)