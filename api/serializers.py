from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','movie_name','desc','year']



class MovieMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','movie_name']