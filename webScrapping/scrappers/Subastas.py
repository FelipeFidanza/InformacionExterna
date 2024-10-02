import requests 
from bs4 import BeautifulSoup

#Página bienal de Venezia
def subastas():
    url = 'https://www.christies.com/en/browse?sortby=relevance'
    response = requests.get(url)

    if response.status_code == 200: #Si puedo acceder a la página
        # Parseo el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Busco los títulos
        titulos_html = soup.find_all('div', class_="css1u3rssc")
        print(titulos_html)
        # Busco la descripción
        descripciones_html = soup.find_all('p', class_="css-1ys2243")
        
        # Busco la imagen
        imagenes_html = soup.find_all('img', class_="css-davmek")

        # Inicializar las listas
        titulos = []
        descripciones = []
        imagenes = []

        # Filtrar la información
        #Titulos
        # for item in titulos_html:
        #     titulos.append(item.text.strip())  # Agregar el texto del titulo a la lista
        # print("\nTítulos filtrados:")
        # for item in titulos:
        #     print(item)

        # #Descripciones
        # for item in descripciones_html:
        #     descripciones.append(item.text.strip())  # Agregar el texto de la descripcion a la lista
        # print("\nDescripciones filtradas: ")
        # for item in descripciones:
        #     print(item)
        
        # #Imagenes
        # for item in imagenes_html:
        #     imagenes.append(item['src'])  # Agregar la fuente de imagen a la lista
        # print("\nImagenes filtradas:")
        # for item in imagenes:
        #     print(item)


        # #Creo el diccionario que va a devolver la función 
        # json_sothebys = {}

        # for i in range(len(titulos)):
        #     subasta = f'subasta{i + 1}'
        #     json_sothebys[subasta] = {
        #         'titulo': titulos[i],
        #         'descripcion': descripciones[i],
        #         'imagen': imagenes[i],
        #         'url': "https://www.sothebys.com/en/buy/auction/2024/modern-discoveries-4?locale=en"
        #     }   
        # print()
        # #Muestro la información
        # print(json_sothebys)


subastas()