from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Wallet, Movement


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'owner', 'label', 'description', 'currency', 'movements')
        read_only_fields = ('owner', 'movements')


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ('id', 'type', 'date', 'amount', 'wallet', 'tags')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'wallets')
