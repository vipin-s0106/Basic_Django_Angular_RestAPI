from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import MovieSerializer,MovieMiniSerializer
from api.models import Movie
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    #here list method is overwrite only when we list the object so we will
    #only return the id and name but during detail we return whole details of movies
    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies,many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        return {'status_code':401,'error':'Some Error occured at baackend site during geting data from table'}

