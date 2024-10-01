from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image', 'url')
        read_only_fields = ('id', )

class AuctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctions
        fields = ('id', 'title', 'author', 'price', 'image', 'url')
        read_only_fields = ('id', )

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ('id', 'title', 'about', 'date', 'image', 'url')
        read_only_fields = ('id', )
        