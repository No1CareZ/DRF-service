from rest_framework import serializers

from .models import Primarch, Chapter


class PrimarchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Primarch
        fields = [
            'pk', 'name', 'homeworld',
            'alive'
        ]


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = [
            'pk', 'name', 'primarch'
        ]
