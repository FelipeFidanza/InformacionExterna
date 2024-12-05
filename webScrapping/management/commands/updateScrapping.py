from django.core.management.base import BaseCommand
from webScrapping.scrappers.news import getNews
from webScrapping.scrappers.auctions import getAuctions
from webScrapping.scrappers.artists import getArtists

class Command(BaseCommand):
    help = 'Run scraping functions to update the database with new data.'

    def handle(self, *args, **kwargs):
        # Llamo a las funciones de scraping
        self.stdout.write("Comenzando el proceso de scrapping...")
        getNews()
        self.stdout.write("Scrapping de noticias completado.")
        
        getAuctions()
        self.stdout.write("Scrapping de subastas completado.")
        
        getArtists()
        self.stdout.write("Scrapping de artistas completado.")
        
        self.stdout.write("Proceso de scrapping completado con éxito.")
