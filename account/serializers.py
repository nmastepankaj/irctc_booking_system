from rest_framework import serializers
import re

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=64)    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()    
    password = serializers.CharField(max_length=64)
