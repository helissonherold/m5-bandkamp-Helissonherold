from django.urls import path
from . import views
from songs.views import SongView

urlpatterns = [
    path(
        "albums/",
        views.ListCreateAlbumView.as_view(),
    ),
    path(
        "albums/<int:albums_id>/songs/",
        SongView.as_view(),
    ),
]
