#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from api.views import ProfileList, ProfileDetail
from api.views import NewsList, NewsDetail
from api.views import ReaderList, ReaderDetail
from api.views import SystemList, SystemDetail
from api.views import ChangeList, ChangeDetail
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

#---------------------------------------------------------
#    Url Paths
#---------------------------------------------------------

urlpatterns = [
    path('profile/', ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('reader/', ReaderList.as_view(), name='reader-list'),
    path('reader/<int:pk>/', ReaderDetail.as_view(), name='reader-detail'),
    path('system/', SystemList.as_view(), name='system-list'),
    path('system/<int:pk>/', SystemDetail.as_view(), name='system-detail'),
    path('change/', ChangeList.as_view(), name='change-list'),
    path('change/<int:pk>/', ChangeDetail.as_view(), name='change-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
