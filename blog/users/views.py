from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView 
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from rest_framework import permissions,status
from .models import Profile
from .serializers import ProfileSerializer,ProfileCreateSerializer,UserCreateSerializer
from django.db.models import Q
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProfileListView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = ProfileSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order-by', '-id')
        queryset = Profile.objects.all().order_by(order_by)
        return queryset
    

class ProfileDetailView(APIView,HitCountMixin):

    def get(self, request, profileName, format=None):
        self.object = get_object_or_404(Profile, username=profileName)
        hit_count = HitCount.objects.get_for_object(self.object)
        hit_count = self.hit_count(request, hit_count)  
        serializer = ProfileSerializer(self.object)
        return Response(serializer.data)


class ProfileSearchView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = ProfileSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', '')
        order_by = self.request.query_params.get('order-by', '-id')
        queryset = Profile.objects.filter(Q(username__icontains = search)|Q(name__icontains = search)).order_by(order_by)
        return queryset


@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class ProfileUpdateView(APIView):

    def patch(self, request, *args, **kwargs):
        self.object = Profile.objects.get(user=request.user)
        serializer = ProfileCreateSerializer(self.object, data=request.data, partial=True)
        if serializer.is_valid():
            updated_profile = serializer.save()
            serializer = ProfileSerializer(updated_profile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class ProfileMe(APIView):

    def get(self,request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)




