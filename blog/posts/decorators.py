from functools import wraps
from rest_framework.exceptions import PermissionDenied
from .models import Post
from django.shortcuts import get_object_or_404

def check_post_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(view, request, *args, **kwargs):
        user = request.user
        post_id = kwargs.get('id')
        post = get_object_or_404(Post, id=post_id)

        if post.user != user:
            raise PermissionDenied("This post does not belong to you.")
        
        return view_func(view, request  , *args, **kwargs)
    
    return _wrapped_view