from celery import shared_task
from .scrappers.news import getNews
from .scrappers.auctions import getAuctions
from .scrappers.artists import getArtists

@shared_task
def updateScrapping():
    # Llamo a las funciones que realizan el web scraping
    getNews()
    getArtists()
    getAuctions()
