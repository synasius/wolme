from __future__ import unicode_literals

from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, views, generics
from rest_framework.response import Response

from .models import Wallet, Movement
from .serializers import WalletSerializer, MovementSerializer, UserSerializer


class WalletViewSet(viewsets.ModelViewSet):
    model = Wallet
    serializer_class = WalletSerializer

    def get_queryset(self):
        user = self.request.user
        return user.wallets.all()

    def pre_save(self, obj):
        obj.owner = self.request.user


class MovementViewSet(viewsets.ModelViewSet):
    model = Movement
    serializer_class = MovementSerializer

    def get_queryset(self):
        return Movement.objects.filter(wallet__owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class MeView(views.APIView):
    """
    This view returns the current user data
    """
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

