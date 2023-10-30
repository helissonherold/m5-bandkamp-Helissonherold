from .models import Song
from albums.models import Album
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        found_album = get_object_or_404(Album, pk=self.kwargs.get("albums_id"))
        return serializer.save(album=found_album)
