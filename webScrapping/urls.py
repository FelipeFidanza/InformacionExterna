from rest_framework import routers
from django.urls import path, re_path, include
from .views import *

router = routers.DefaultRouter()

#router.register(r'api/news', NewsViewSet, basename='news')
#router.register(r'api/auctions', AuctionsViewSet, basename='auctions')
#router.register(r'api/artists', ArtistsViewSet, basename='artists')

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('api/verNoticias', viewNews, name='Noticias'),
    path('api/verSubastas', viewAuctions, name='Subastas'),
    path('api/verArtistas', viewArtists, name='Artistas'),
]