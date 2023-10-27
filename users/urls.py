from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(
        "users/",
        views.ListCreateUserView.as_view(),
    ),
    path(
        "users/<int:pk>/",
        views.RetrieveUpdateDeleteUserView.as_view(),
    ),
    path("users/login/", TokenObtainPairView.as_view()),
    # path("login/refresh/", TokenRefreshView.as_view()),
]
# from django.urls import path
# from . import views
# from rest_framework_simplejwt import views as jwt_views

# urlpatterns = [
#     path("users/", views.UserView.as_view()),
#     path("users/<int:pk>/", views.UserDetailView.as_view()),
#     path("users/login/", jwt_views.TokenObtainPairView.as_view()),
# ]
