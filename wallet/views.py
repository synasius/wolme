# Create your views here.
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from wallet.models import Wallet
from wallet.serializers import WalletSerializer, UserSerializer
from wallet.permissions import IsOwnerOrReadOnly


class WalletList(generics.ListCreateAPIView):
    model = Wallet
    serializer_class = WalletSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.user = self.request.user


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Wallet
    serializer_class = WalletSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
