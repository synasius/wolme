from django.forms import widgets
from rest_framework import serializers
from wallet.models import Wallet


class WalletSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    # user = serializers.PrimaryKeyRelatedField()
    user_id = serializers.IntegerField()
    label = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)

    currency = serializers.ChoiceField(choices=Wallet.CURRENCIES, default="EUR")

    # back relationships
    # movements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.user_id = attrs.get('user', instance.user_id)
            instance.label = attrs.get('label', instance.label)
            instance.description = attrs.get('description', instance.description)
            instance.currency = attrs.get('currency', instance.currency)

            return instance

        # Create new instance
        return Wallet(**attrs)
