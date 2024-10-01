from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()   # pylint: disable=no-member
    serializer_class = NewsSerializer
    permissions_classes = [permissions.AllowAny]

class AuctionsViewSet(viewsets.ModelViewSet):
    queryset = Auctions.objects.all()   # pylint: disable=no-member
    serializer_class = AuctionsSerializer
    permissions_classes = [permissions.AllowAny]

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()   # pylint: disable=no-member
    serializer_class = ArtistsSerializer
    permissions_classes = [permissions.AllowAny]