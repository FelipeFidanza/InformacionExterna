import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

# Para traducir los títulos y descripciones
translator = Translator()

# Página InfoDesigners
def infoDesigners():
    url = 'https://www.infodesigners.eu/'

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Verifica si hubo un error en la respuesta HTTP

        if response.status_code == 200: #Si puedo acceder a la página
            # Parseo el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')

            # Busco los títulos
            titles_html = soup.find_all('h3', itemprop="name")

            # Busco la descripción
            descriptions_html = soup.find_all('p', itemprop="description")

            # Busco la imagen
            images_html = soup.find_all('img', itemprop="image")

            # Busco la URL de la noticia
            urls_html = soup.find_all('a')

            # Inicializar las listas
            titles = []
            descriptions = []
            images = []
            urls_temp = []
            urls = []

            # Filtrar la información
            #Titulos
            for item in titles_html:
                titles.append(item.text.strip())  # Agregar el texto del titulo a la lista
            for i in range(len(titles)):
                string = str(translator.translate(str(titles[i]), dest='es')) #Traduzco

                part_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
                name = part_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

                titles[i] = name

            # print("\nTítulos filtrados:")
            # for item in titles:
            #     print(item)

            #Descripciones
            for item in descriptions_html:
                descriptions.append(item.text.strip())  # Agregar el texto de la descripcion a la lista
            for i in range(len(descriptions)):
                string = str(translator.translate(str(descriptions[i]), dest='es')) #Traduzco

                part_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
                name = part_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

                descriptions[i] = name

            # print("\nDescripciones filtradas:")
            # for item in descriptions:
            #     print(item)


            #Imagenes
            for item in images_html:
                images.append(item['src'])  # Agregar la fuente de imagen a la lista
            for i in range(len(images)):    # Agrego la ruta a cada imagen
                images[i]= "https://www.infodesigners.eu"+str(images[i])

            # print("\nImagenes filtradas:")
            # for item in images:
            #     print(item)


            #Urls
            for item in urls_html:
                if re.findall(r'^competitions/\w+-', item['href']):
                    urls_temp.append(item['href'])
            for item in urls_temp:
                if item not in urls:
                    urls.append(item)
            for i in range(len(urls)):  #Agrego la ruta a cada url
                urls[i] = "https://www.infodesigners.eu/"+str(urls[i])

            # print("\nUrls filtradas:")
            # for item in urls:
            #     print(item)


            #Devuelvo un diccionario (formato json)
            return {
                "titles": titles,
                "descriptions": descriptions,
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