from django.shortcuts import get_object_or_404, render
from .models import Post, Category, Tag
from rest_framework.views import APIView
from rest_framework import authentication, permissions,status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import *
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView 
from django.db.models import Q
from .decorators import check_post_owner
from .models import Comment
from users.models import CustomUser


class PostListView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer
       
    def get_queryset(self):
        order_by = self.request.query_params.get('order-by', '-id')
        queryset = Post.objects.all().order_by(order_by)
        return queryset


class PostSearchView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer
       
    def get_queryset(self):
        search = self.request.query_params.get('search', '')
        order_by = self.request.query_params.get('order-by', '-id')
        queryset = Post.objects.filter(Q(title__icontains = search)|Q(content__icontains = search)|Q(tags__name__icontains = search)).order_by(order_by)
        return queryset


class PostListUser(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer

    def get_queryset(self, format=None):
        user = CustomUser.objects.get(username = self.kwargs['username'])
        queryset = Post.objects.filter(user=user).order_by('-id')
        return queryset


class PostDetailView(APIView,HitCountMixin):

    def get(self, request, postId, format=None):
        self.object = get_object_or_404(Post, id=postId)
        hit_count = HitCount.objects.get_for_object(self.object)
        hit_count = self.hit_count(request, hit_count)  
        serializer = PostSerializer(self.object)
        return Response(serializer.data)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class PostCreateView(APIView):

    def post(self, request, format=None):
        serializer = PostCreateSerializer(data =  request.data, context={'request': request})
        if serializer.is_valid():
            post = serializer.save()     
            return Response(post.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class PostUpdateView(APIView):

    @check_post_owner
    def patch(self, request, postId, *args, **kwargs):
        self.object = Post.objects.get(id=postId)
        serializer = PostCreateSerializer(self.object, data=request.data, partial=True)
        if serializer.is_valid():
            updated_post = serializer.save()
            return Response(updated_post.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class PostDeleteView(APIView):

    @check_post_owner
    def delete(self, request, postId, *args, **kwargs):
        self.object = Post.objects.get(id=postId)
        self.object.delete()
        return Response({"message": "Post deleted successfully."}, status=200)


class TagListView(ListAPIView):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryListView(ListAPIView):
    pagination_class = None
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(APIView):

    def get(self, request, slug, format=None):
        self.object = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(category=self.object).order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class TagDetailView(APIView):

    def get(self, request, slug, format=None):
        self.object = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tags=self.object).order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostListCommentsView(ListAPIView):
    pagination_class = None
    serializer_class = CommentSerializer
    queryset = Comment.objects.root_nodes()


class CommentCreateView(APIView):

    def post(self,request,format=None):
        serializer = CommentCreateSerializer(data =  request.data, context={'request': request})
        if serializer.is_valid():
            comment = serializer.save()     
            return Response(comment.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
