# todos/serializers.py
from rest_framework import serializers
from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'card_number',
            'pin',
            'amount',
        )
        model = UserAccount
