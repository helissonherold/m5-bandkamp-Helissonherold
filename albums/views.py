from .models import Album
from .serializers import AlbumSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateAlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUpdateDeleteAlbumView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_url_kwarg = "album_id"
