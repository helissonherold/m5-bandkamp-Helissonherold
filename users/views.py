from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
