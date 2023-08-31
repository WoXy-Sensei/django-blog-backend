from rest_framework import serializers,status
from rest_framework.response import Response
from hitcount.models import HitCount
from .models import *
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from rest_framework_recursive.fields import RecursiveField
from rest_framework_recaptcha.fields import ReCaptchaField


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("name","slug","post_count")  


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
            "post_count"
        )


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    tags = serializers.CharField()

    class Meta:
        model = Post
        fields = (
            'user',
            "title",
            "content",
            "image",
            "category",
            "tags", 
        )

   
    def create(self,validated_data):
        tags = validated_data.pop('tags')
        validated_data['user'] = self.context['request'].user
        validated_data['category'] =  get_object_or_404(Category,name=validated_data['category'])
        
 
        post = Post.objects.create(**validated_data)    
        post.set_tags(tags)
        post.save()
            
        return PostSerializer(post)
    

    def update(self,instance,validated_data):
        post = instance

        if 'category' in validated_data:
            validated_data['category'] = get_object_or_404(Category,name=validated_data['category'])

        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
            post.set_tags(tags)

        for field in validated_data:
            setattr(post,field,validated_data[field])   

        post.save()

        return PostSerializer(post)
    

class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()
    hits = serializers.IntegerField(source = "hits_count")

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            "title",
            "content",
            "image",
            "category",
            "tags",
            "slug",
            "publish_date",
            'hits'
        )


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveField(many=True)

    class Meta:
        model = Comment
        fields = ('id','name','content','post','parent','publish_date','replies')


class CommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.IntegerField()
    recaptcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('name','content','post','parent','recaptcha')


    def create(self,validated_data):
        validated_data.pop('recaptcha')
        validated_data['post'] = get_object_or_404(Post,id=validated_data['post'])
        if not 'parent' in validated_data:
            validated_data['parent'] = None
        comment = Comment.objects.create(**validated_data)    
        comment.save()
            
        return CommentSerializer(comment)
