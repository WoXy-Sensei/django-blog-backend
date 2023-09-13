from django.urls import path
from .views import *


urlpatterns = [
    
    path('', PostListView.as_view() , name="index"),
    path('search', PostSearchView.as_view(), name="post_search"),
    path('create', PostCreateView.as_view(), name="post_create"),
    path('<slug:postSlug>', PostDetailBySlugView.as_view(), name="detail_slug_post"),
    path('user/<str:username>', PostListUser.as_view(), name="post_user"),
    path('<int:postId>', PostDetailByIdView.as_view(), name="detail_id_post"),
    path('<int:postId>/comments', PostListCommentsView.as_view(), name="post_detail"),
    path('<int:postId>/update', PostUpdateView.as_view(), name="post_update"),
    path('<int:postId>/delete', PostDeleteView.as_view(), name="post_delete"),

    path('category', CategoryListView.as_view(), name="category_list"),
    path('category/<slug:slug>', CategoryDetailView.as_view(), name="category_detail"),

    path('tags', TagListView.as_view(), name="list_tag"),
    path('tags/<slug:slug>', TagDetailView.as_view(), name="tag_detail"),

    
    path('comments/create', CommentCreateView.as_view(), name="comment_create"),
    
]
