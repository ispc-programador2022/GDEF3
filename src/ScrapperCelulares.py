from bs4 import BeautifulSoup
import requests
from Modelos import Celular


sitioWeb = 'https://www.musimundo.com/compare-products/compare?pcodes=00556015&pcodes=00591011&pcodes=00434006'


def getContenidoHtml(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido, 'lxml')
    return soup

def getCelularesConInfoPpal(soup):

    boxPrincipalCelulares = soup.find('div', class_='productGrid completeCompareItem clearfix')

    boxCelulares = []
    boxCelular1 = boxPrincipalCelulares.find('div', class_='col span_4 first')
    boxCelulares.append(boxCelular1)
    boxCelular2 = boxPrincipalCelulares.find('div', class_='col span_4')
    boxCelulares.append(boxCelular2)
    boxCelular3 = boxPrincipalCelulares.find('div', class_='col span_4 last')
    boxCelulares.append(boxCelular3)

    celulares = []
    for boxCelular in boxCelulares:
        marca = boxCelular.find('div', class_='mus-pro-brand').find('span').get_text()
        nombre = boxCelular.find('p', class_='mus-pro-name').get_text().replace("\t", "")
        codigo = boxCelular.find('p', class_='mus-pro-code').get_text()
        precio = boxCelular.find('span', class_='mus-pro-price-number').find('span').get_text()

        celular = Celular(marca, nombre, codigo, precio)
        celulares.append(celular)
    return celulares



soup = getContenidoHtml(sitioWeb)
celulares = getCelularesConInfoPpal(soup)
for c in celulares:
    print(c.__str__())





# Prueba de cómo obtener los datos de las tablas..
# falta colocar en método y sacar datos.

detalles = soup.find('div', class_='productDetailClass')
tablaAtributos = detalles.find('table')
tablaCaract = tablaAtributos.find_next_sibling().find_next_sibling()

print("...................................")
print(tablaAtributos.prettify())
print("...................................")
print(tablaCaract.prettify())