#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from api.serializers import ProfileSerializer, NewsSerializer, ReaderSerializer, SystemSerializer, ChangeSerializer
from dashboard.models import Profile, News, Reader, System, Change
from rest_framework import generics

#---------------------------------------------------------
#    Classes
#---------------------------------------------------------

class ProfileList(generics.ListCreateAPIView):
    """
    List or create a profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class NewsList(generics.ListCreateAPIView):
    """
    List or create a new.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a new.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ReaderList(generics.ListCreateAPIView):
    """
    List or create a reader.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a reader.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class SystemList(generics.ListCreateAPIView):
    """
    List or create a system.
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a system.
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class ChangeList(generics.ListCreateAPIView):
    """
    List or create a change.
    """
    queryset = Change.objects.all()
    serializer_class = ChangeSerializer


class ChangeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a change.
    """
    queryset = Change.objects.all()
    serializer_class = ChangeSerializer
