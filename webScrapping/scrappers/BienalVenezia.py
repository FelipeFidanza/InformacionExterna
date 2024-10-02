import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

# Para traducir los títulos y descripciones
traductor = Translator()

#Página bienal de Venezia
def bienalVenezia():
    url = 'https://www.labiennale.org/en'
    response = requests.get(url)

    if response.status_code == 200: #Si puedo acceder a la página
        # Parseo el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Busco los títulos
        titulos_html = soup.find_all('div', class_="lb-item-title")
        
        # Busco la descripción
        descripciones_html = soup.find_all('div', class_="lb-excerpt")
        
        # Busco la imagen
        imagenes_html = soup.find_all('img', class_="lb-media")

        # Busco la URL de la noticia
        urls_html = soup.find_all('a', class_="lb-entry-link lb-base-content lb-slide-link")
        
        # Inicializar las listas
        titulos = []
        descripciones = []
        imagenes = []
        urls = []

        # Filtrar la información
        #Titulos
        for item in titulos_html:
            titulos.append(item.text.strip())  # Agregar el texto del titulo a la lista
        for i in range(len(titulos)):
            string = str(traductor.translate(str(titulos[i]), dest='es')) #Traduzco

            parte_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
            nombre = parte_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

            titulos[i] = nombre
        print("\nTítulos filtrados:")
        for item in titulos:
            print(item)

        #Descripciones
        for item in descripciones_html:
            descripciones.append(item.text.strip())  # Agregar el texto de la descripcion a la lista
        eliminar=len(descripciones) - len(titulos)
        descripciones = descripciones[:-eliminar] #Elimino las descripciones que sobran
        for i in range(len(descripciones)):
            string = str(traductor.translate(str(descripciones[i]), dest='es')) #Traduzco
            
            parte_1 = string.split('text=')[1]  # Tomar la parte después de 'text='
            nombre = parte_1.split(', pronunciation=')[0] # Tomar la parte antes de ', pronunciation='

            descripciones[i] = nombre
        print("\nDescripciones filtradas: ")
        for item in descripciones:
            print(item)
        
        #Imagenes
        for item in imagenes_html:
            imagenes.append(item['src'])  # Agregar la fuente de imagen a la lista
        print("\nImagenes filtradas:")
        for item in imagenes:
            print(item)
        
        #Urls
        for item in urls_html:
            urls.append(item['href'])
        for i in range(len(urls)):  #Agrego la ruta a cada url
            urls[i] = "https://www.labiennale.org"+str(urls[i])
        print("\nUrls filtradas:")
        for item in urls:
            print(item)

        #Creo el diccionario que va a devolver la función 
        json_bienalVenezia = {}
        for i in range(len(titulos)):
            noticia = f'noticia{i + 1}'
            json_bienalVenezia[noticia] = {
                'titulo': titulos[i],
                'descripcion': descripciones[i],
                'imagen': imagenes[i],
                'url': urls[i]
            }   
        print()
        #Muestro la información
        print(json_bienalVenezia)
