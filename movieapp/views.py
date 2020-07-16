from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer


class IndexView(APIView):

    allowed_methods = ['GET']
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        director = request.query_params.get('director', None)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)

        genre = request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genre__name__icontains=genre)

        director = request.query_params.get('director', None)
        if director is not None:
            queryset = queryset.filter(director__icontains=director)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
