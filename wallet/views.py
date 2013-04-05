# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from wallet.models import Wallet
from wallet.serializers import WalletSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def wallet_list(request):
    """
    List all wallets, or create a new wallet
    """
    if request.method == "GET":
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return JSONResponse(serializer.data)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = WalletSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def wallet_detail(request, pk):
    """
    Retrieve, update or delete a wallet
    """
    try:
        snippet = Wallet.objects.get(pk=pk)
    except Wallet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WalletSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WalletSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
