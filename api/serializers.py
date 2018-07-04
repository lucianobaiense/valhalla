#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from rest_framework import serializers
from dashboard.models import Profile, News, Reader, System, Change

#---------------------------------------------------------
#    Serializers
#---------------------------------------------------------

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'


class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'
