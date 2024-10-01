from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'api/news', NewsViewSet, basename='news')
router.register(r'api/auctions', AuctionsViewSet, basename='auctions')
router.register(r'api/artists', ArtistsViewSet, basename='artists')

urlpatterns = router.urls

