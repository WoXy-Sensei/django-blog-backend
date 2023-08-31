from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Profile

class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'email','birthdate','password')


class ProfileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('name','biography','image')
    
    


class ProfileSerializer(serializers.ModelSerializer):
    hits = serializers.IntegerField(source = "hits_count")

    class Meta:
        model = Profile
        fields = ('username','name','biography','image','hits')