import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

#Inicializo el traductor
translator = Translator()

#Página de subastas (Christies):
def auctions():
    url = 'https://www.christies.com/en/browse?filterids=%7CCoaCategoryValues%7BAll%2Bother%2Bcategories%2Bof%2Bobjects%7D%7C&sortby=relevance'

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Verifica si hubo un error en la respuesta HTTP

        if response.status_code == 200: #Si puedo acceder a la página
            # Parseo el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Busco los autores
            authors_html = soup.find_all('h3', class_="chr-lot-tile__primary-title ellipsis--two-lines")
            
            # Busco los titulos
            titles_html = soup.find_all('p', class_="chr-lot-tile__secondary-title ellipsis--one-line")
            
            # Busco los precios
            text_html = str(soup)
            #patron = r'(USD|EUR)\s([\d,]+)\s-\s([\d,]+)'
            patron = r'(USD|EUR|HKD)(\s[\d,]+\s-\s[\d,]+)'
            prices = re.findall(patron, text_html)
            
            # Busco las imagenes
            images_html = soup.find_all('div', class_="chr-lot-tile__image")
            
            # Busco las URLs de las noticias
            urls_html = soup.find_all('a', class_="chr-lot-tile__link")
            
            # Inicializar las listas
            titles = []
            authors = []
            images = []
            urls = []

            # Filtrar la información
            #Titulos
            for item in titles_html:
                titles.append(item.text.strip())  # Agregar el texto del titulo a la lista
            titles = titles[:30]
            #print("\nTítulos filtrados:")
            #for item in titles:
            #    print(item)


            #Autores
            for item in authors_html:
                authors.append(item.text.strip())  # Agregar el autor a la lista
            authors = authors[:30]
            #print("\nAutores filtrados:")
            #for item in authors:
            #    print(item)


            #Precios
            prices = prices[:30]
            for i in range(30):
                prices[i] = str(prices[i][0]) + str(prices[i][1])
            #print("\nPrecios filtrados:")
            #for item in prices:
            #    print(item)
            

            #Imagenes
            images_html = images_html[:30]
            images_html = str(images_html)
            pattern = r'http[s]?://[\.\w]+christies\.com[\w\(\)\.\?\=\-\/\s]+'
            images = re.findall(pattern, images_html)
            #print("\nImagenes filtradas:")
            #for item in images:
            #    print(item)


            #Urls
            urls_html = urls_html[:30]
            urls_html = str(urls_html)
            pattern = r'http[s]?://[\w\.\/]+christies\.com/[\w\?\=\.\-\/\&\;]+'
            urls = re.findall(pattern, urls_html)
            #print("\nUrls filtradas:")
            #for item in urls:
            #    print(item)


            #Devuelvo un diccionario (formato json)
            return {
                "titles": titles,
                "authors": authors,
                "prices" : prices,
                "images": images,
                "urls": urls,
            }

        else:       #Si no logro acceder a la página
            return {}
        
    except requests.exceptions.ConnectionError:
        return {}
    except requests.exceptions.Timeout:
        return {}
    except requests.exceptions.HTTPError:
        return {}
    except requests.exceptions.InvalidURL:
        return {}
    except requests.exceptions.RequestException:
        return {}
    



import sys
import os
import django

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Establece el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InfoExterna.settings')

# Inicializa Django
django.setup()


#auctions()

from webScrapping.models import Auctions

def getAuctions():

    # Llamo a las funciones de las subastas
    dicAuctions = auctions()

    # Creo listas con la información de cada atributo de las subastas
    auctionsTitles = dicAuctions["titles"]
    auctionsAuthors = dicAuctions["authors"]
    auctionsPrices = dicAuctions["prices"]
    auctionsImages = dicAuctions["images"]
    auctionsUrls = dicAuctions["urls"]
    
    # Cargo las subastas a la base de datos
    for i, title in enumerate(auctionsTitles):
        # Verifico que no esté cargada la subasta
        if not Auctions.objects.filter(title=title, url=auctionsUrls[i]).exists(): # pylint: disable=no-member
            # Si no está cargada, la agrego a la base de datos
            Auctions.objects.create( #pylint: disable=no-member
                title=title,
                author=auctionsAuthors[i],
                price=auctionsPrices[i],
                image=auctionsImages[i],
                url=auctionsUrls[i])

getAuctions()