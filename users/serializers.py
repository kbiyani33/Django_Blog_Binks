"""
Serialization is the process of converting complex objects into a data format that can be easily stored or transmitted. 
In the context of the Django Rest Framework, Serialization is used to convert the data in your Django models into a format that can be sent over the internet and used by other applications.

Here are some specific reasons why Serialization is essential in the Django Rest Framework:

It allows you to convert your Django models and querysets into formats like JSON or XML, which can be easily consumed by other applications or JavaScript frameworks on the frontend.

It allows you to control exactly what data is exposed by your API and how it is formatted. 
This is important for security and for ensuring that your API is consistent and easy to use.

It allows you to easily convert complex data structures into a format that can be easily stored or transmitted. 
This is particularly useful when working with large datasets or when dealing with data that has a lot of relationships between different objects.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
