from django.forms import widgets
from rest_framework import serializers
from wallet.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    # back relationships
    movements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'label', 'description', 'currency', 'movements')
