from .models import Song
from albums.models import Album
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

# from rest_framework.views import APIView, Response, status, Request
# from rest_framework.pagination import PageNumberPagination


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    pagination_class = PageNumberPagination

    # def get_queryset(self):
    #     found_album = get_object_or_404(Album, pk=self.kwargs.get("album_id"))
    #     return Song.objects.filter(album=found_album)

    def perform_create(self, serializer):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("albums_id"))
        return serializer.save(album=found_album)


# class SongView(APIView, PageNumberPagination):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request, pk):
#         """
#         Obtençao de musicas
#         """
#         songs = Song.objects.filter(album_id=pk)

#         result_page = self.paginate_queryset(songs, request)
#         serializer = SongSerializer(result_page, many=True)

#         return self.get_paginated_response(serializer.data)

#     def post(self, request, pk):
#         """
#         Criaçao de musica
#         """
#         album = get_object_or_404(Album, pk=pk)

#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(album=album)

#         return Response(serializer.data, status.HTTP_201_CREATED)
