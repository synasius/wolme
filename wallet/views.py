# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wallet.models import Wallet
from wallet.serializers import WalletSerializer


@api_view("GET", "POST")
def wallet_list(request):
    """
    List all wallets, or create a new wallet
    """
    if request.method == "GET":
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = WalletSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view("GET", "PUT", "DELETE")
def wallet_detail(request, pk):
    """
    Retrieve, update or delete a wallet
    """
    try:
        snippet = Wallet.objects.get(pk=pk)
    except Wallet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WalletSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WalletSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
