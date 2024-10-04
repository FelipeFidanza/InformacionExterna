import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

# Inicializo traductor
translator = Translator()


# Página de artistas
def artists():
    url = 'https://www.artnews.com/c/art-news/artists/'

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        if response.status_code == 200: # Verifico si puedo acceder a la página
            # Parseo el contenido
            soup = BeautifulSoup(response.text, 'html.parser')

            #Busco los titulos
            #titles_html = soup.find_all('div', class_="a-span2 lrv-u-flex lrv-u-flex-direction-column lrv-u-height-100p lrv-u-justify-content-center")
            titles_html = soup.find_all('h3', class_="c-title lrv-u-font-size-14 lrv-u-font-size-26@tablet lrv-u-font-size-32@desktop lrv-u-font-family-primary lrv-u-display-block u-font-weight-normal@mobile-max lrv-u-line-height-small lrv-u-margin-b-050", id="")

            #Busco los about
            about_html = soup.find_all('div', class_="c-dek lrv-u-font-weight-light lrv-u-font-size-16 lrv-u-font-size-18@desktop-xl a-hidden@mobile-max lrv-u-margin-a-00")

            #Busco las fechas
            dates_html = soup.find_all('time', class_="c-timestamp", datetime="")

            #Busco las imagenes
            images_html = soup.find_all('div', class_="lrv-a-crop-2x3", style="")

            #Busco las urls
            urls_html = soup.find_all('h3', class_="c-title lrv-u-font-size-14 lrv-u-font-size-26@tablet lrv-u-font-size-32@desktop lrv-u-font-family-primary lrv-u-display-block u-font-weight-normal@mobile-max lrv-u-line-height-small lrv-u-margin-b-050", id="")


            # Creo las listas
            titles = []
            about = []
            dates = []
            images = []
            urls = []

            # Filtro la información

            #Titulos
            for item in titles_html:
                titles.append(item.text.strip())
            for i in range(len(titles)):
                string = str(translator.translate(str(titles[i]), dest='es')) #Traduzco

                part_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
                name = part_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

                titles[i] = name
            # print("\nTítulos filtrados:")
            # for item in titles:
            #     print(item)


            #Acerca de
            for item in about_html:
                about.append(item.text.strip())
            for i in range(len(about)):
                string = str(translator.translate(str(about[i]), dest='es')) #Traduzco

                part_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
                name = part_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

                about[i] = name
            # print("\nDescripciones filtradas:")
            # for item in about:
            #     print(item)


            #Fechas
            for item in dates_html:
                dates.append(item.text.strip())
            # print("\nFechas filtradas:")
            # for item in dates:
            #     print(item)


            #Imágenes
            images_html = images_html[1:]
            pattern = r'https://www\.artnews\.com/wp-content/uploads/[\w\-\.\=\?\%\&\;\/\#\$\"\!]+'
            images = re.findall(pattern, str(images_html))
            images = images[::2]
            # print("\nImagenes filtradas")
            # for item in images:
            #     print(item)


            #Urls
            pattern = r'https://www\.artnews\.com/[\w\/\-\.\=\?\%\&\;\#\$\"\!]+'
            urls = re.findall(pattern, str(urls_html))
            # print("\nUrls filtradas:")
            # for item in urls:
            #     print(item)


            #Devuelvo el json
            return {
                "titles" : titles,
                "about" : about,
                "dates" : dates,
                "images": images,
                "urls" : urls,
            }

        else:       #Si no puedo entrar a la página
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


from webScrapping.models import Artists

def getArtists():

    # Llamo a las funciones de las subastas
    dicArtists = artists()

    # Creo listas con la información de cada atributo de las subastas
    artistsTitles = dicArtists["titles"]
    artistsAbout = dicArtists["about"]
    artistsDates = dicArtists["dates"]
    artistsImages = dicArtists["images"]
    artistsUrls = dicArtists["urls"]
    
    # Cargo las subastas a la base de datos
    for i, title in enumerate(artistsTitles):
        Artists.objects.create( #pylint: disable=no-member
            title=title,
            about=artistsAbout[i],
            date=artistsDates[i],
            image=artistsImages[i],
            url=artistsUrls[i])
        