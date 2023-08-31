from django.urls import include, path
from .views import *

app_name = "users"
urlpatterns = [

    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('profiles',ProfileListView.as_view(),name='profiles_list'),
    path('profiles/me',ProfileMe.as_view(),name='profiles_me'),
    path('profiles/me/update',ProfileUpdateView.as_view(),name='profiles_update'),
    path('profiles/search',ProfileSearchView.as_view(),name='profiles_search'),
    path('profiles/<str:profileName>',ProfileDetailView.as_view(),name='profiles_detail')
    
]
