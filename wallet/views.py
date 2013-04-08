# Create your views here.
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class WalletList(APIView):
    """
    List all wallets, or create a new wallet
    """
    def get(self, request, format=None):
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WalletSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetail(APIView):
    """
    Retrieve, update or delete a wallet
    """
    def get_object(self, pk):
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        wallet = self.get_object(pk)
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
