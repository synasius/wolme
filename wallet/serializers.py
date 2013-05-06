from django.contrib.auth.models import User

from rest_framework import serializers

from wallet.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    # back relationships
    movements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.Field(source="user.username")

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'label', 'description', 'currency', 'movements')


class UserSerializer(serializers.ModelSerializer):
    wallets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'wallets')
