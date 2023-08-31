from django.contrib import admin
from .models import *
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ['title','publish_date']
    search_fields = ['title','content']
    list_filter = ['publish_date','user']

    class Meta:
        model = Post



admin.site.register(Post,AdminPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)