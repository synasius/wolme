# Create your views here.
from rest_framework import generics

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletList(generics.ListCreateAPIView):
    model = Wallet
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Wallet
    serializer_class = WalletSerializer
