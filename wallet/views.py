# Create your views here.
from django.http import Http404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.MultipleObjectAPIView):
    model = Wallet
    serializer_class = WalletSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WalletDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.SingleObjectAPIView):
    model = Wallet
    serializer_class = WalletSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
