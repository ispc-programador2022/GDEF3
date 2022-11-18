from bs4 import BeautifulSoup
import requests
import pandas as pd
from Models import Panial


pagWeb = 'https://www.farmaonline.com/bebe---maternidad/panales-para-Bebe'

# Obtiene el contenido html de la página web
def getContenidoHtml(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido, 'lxml')
    return soup

# Obtiene información de cada producto
def getPaniales(soup):

    box = soup.find('div', class_ = 'prateleira vitrine n48colunas')
    boxPaniales = box.find_all('li', class_ = 'productos-para-bebes-y-maternidad-|-farmaonline')
    paniales = list()

    # Selecciona la info de cada producto, genera un objeto Panial() y lo guarda en una lista
    for panial in boxPaniales:
        descripcion = panial.find('h3', class_='product-name').find('a').get_text().split()
        
        marca = panial.find('div', class_='brand').get_text().replace("\n", "").replace(" ", "")
        tipo = (descripcion[1] + " " + descripcion[2] + " " + descripcion[3]).replace(" talle", "")
        tamanio = descripcion[-3]
        cantidad = descripcion[-2].replace("(", "")
        precioText = panial.find('span', class_='best-price').get_text().replace("\n", "").replace(" ", "")
        precio = precioText.replace("$", "").replace(".", "").replace(",", ".")

        panial = Panial(marca, tipo, tamanio, cantidad, precio)
        paniales.append(panial)
    return paniales

soup = getContenidoHtml(pagWeb)
paniales = getPaniales(soup)

listadoDePaniales = []
for p in paniales:
    listadoDePaniales.append(p.listarContenido())

dfPaniales = pd.DataFrame(listadoDePaniales, columns=['Marca', 'Tipo', 'Tamaño', 'Cantidad', 'Precio', 'Precio por Un'])

print(dfPaniales)
dfPaniales.to_csv("PañalesFarmaOnline.csv", index=False)