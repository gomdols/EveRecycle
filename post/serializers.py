from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'board_name',
            'board_type',
        )
        model = Board