import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

#Inicializo el traductor
translator = Translator()

#Página de subastas (Christies):
def Auctions():
    url = 'https://www.christies.com/en/browse?sortby=relevance'

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Verifica si hubo un error en la respuesta HTTP

        if response.status_code == 200: #Si puedo acceder a la página
            # Parseo el contenido HTML de la página
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Busco los títulos
            authors_html = soup.find_all('h3', class_="chr-lot-tile__primary-title ellipsis--two-lines")
            
            # Busco los autores
            titles_html = soup.find_all('p', class_="chr-lot-tile__secondary-title ellipsis--one-line")
            
            # Busco los precios
            text_html = str(soup)
            #patron = r'(USD|EUR)\s([\d,]+)\s-\s([\d,]+)'
            patron = r'(USD|EUR)(\s[\d,]+\s-\s[\d,]+)'
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
            # print("\nTítulos filtrados:")
            # for item in titles:
            #     print(item)


            #Autores
            for item in authors_html:
                authors.append(item.text.strip())  # Agregar el autor a la lista
            authors = authors[:30]
            # print("\nAutores filtrados:")
            # for item in authors:
            #     print(item)


            #Precios
            prices = prices[:30]
            for i in range(30):
                prices[i] = str(prices[i][0]) + str(prices[i][1])
            # print("\nPrecios filtrados:")
            # for item in prices:
            #     print(item)
            

            #Imagenes
            images_html = images_html[:30]
            images_html = str(images_html)
            pattern = r'http[s]?://www\.christies\.com/img/lotimages/[\w\(\)\.\?\=\-\/]+'
            images = re.findall(pattern, images_html)
            # print("\nImagenes filtradas:")
            # for item in images:
            #     print(item)


            #Urls
            urls_html = urls_html[:30]
            urls_html = str(urls_html)
            pattern = r'http[s]?://onlineonly\.christies\.com/[\w\?\=\.\&\;]+'
            urls = re.findall(pattern, urls_html)
            # print("\nUrls filtradas:")
            # for item in urls:
            #     print(item)


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
