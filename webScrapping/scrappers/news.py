import sys
import os
import django
from webScrapping.models import News
from .bienalVenezia import bienalVenezia
from .infoDesigners import infoDesigners

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Establece el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InfoExterna.settings')

# Inicializa Django
django.setup()


def getNews():

    # Llamo a las funciones de los archivos de noticias
    dicBienalVenezia = bienalVenezia()
    dicInfoDesigners = infoDesigners()

    # Creo listas con la información de cada atributo de las noticias
    newsTitles = dicBienalVenezia["titles"]
    newsDescriptions = dicBienalVenezia["descriptions"]
    newsImages = dicBienalVenezia["images"]
    newsUrls = dicBienalVenezia["urls"]

    # Agrego todas las noticias a las listas
    newsTitles.extend(dicInfoDesigners["titles"])
    newsDescriptions.extend(dicInfoDesigners["descriptions"])
    newsImages.extend(dicInfoDesigners["images"])
    newsUrls.extend(dicInfoDesigners["urls"])
    
    # Cargo las noticias a la base de datos
    for i, title in enumerate(newsTitles):
        # Verifico si ya existe la noticia en cuestión
        if not News.objects.filter(title=title, url=newsUrls[i]).exists():   # pylint: disable=no-member
            # En caso de no existir, la agrego a la base de datos
            News.objects.create( #pylint: disable=no-member
                title=title,
                description=newsDescriptions[i],
                image=newsImages[i],
                url=newsUrls[i])
            
getNews()
