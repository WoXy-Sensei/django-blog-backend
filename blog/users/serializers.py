from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Profile,CustomUser
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class ProfileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('name','biography','image')
    
    
class ProfileSerializer(serializers.ModelSerializer):
    hits = serializers.IntegerField(source = "hits_count")

    class Meta:
        model = Profile
        fields = ('username','name','biography','image','hits')