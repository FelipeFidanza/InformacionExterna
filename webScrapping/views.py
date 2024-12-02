# from django.shortcuts import render
# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# from rest_framework import viewsets, permissions
from .serializers import *


# Create your views here.

# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()   # pylint: disable=no-member
#     serializer_class = NewsSerializer
#     permissions_classes = [permissions.AllowAny]

# class AuctionsViewSet(viewsets.ModelViewSet):
#     queryset = Auctions.objects.all()   # pylint: disable=no-member
#     serializer_class = AuctionsSerializer
#     permissions_classes = [permissions.AllowAny]

# class ArtistsViewSet(viewsets.ModelViewSet):
#     queryset = Artists.objects.all()   # pylint: disable=no-member
#     serializer_class = ArtistsSerializer
#     permissions_classes = [permissions.AllowAny]


@api_view(['GET'])
def viewNews(request):
    news = News.objects.all() # pylint: disable=no-member
    serializer = NewsSerializer(news, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def viewAuctions(request):
    auctions = Auctions.objects.all() # pylint: disable=no-member
    serializer = AuctionsSerializer(auctions, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def viewArtists(request):
    artists = Artists.objects.all() # pylint: disable=no-member
    serializer = ArtistsSerializer(artists, many = True)
    return Response(serializer.data)