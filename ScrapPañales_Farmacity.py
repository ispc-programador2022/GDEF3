from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.farmacity.com/bebes/higiene-del-bebe/panales?PS=21&O=OrderByPriceASC'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Pañales = ps

ps = soup.find_all('div', class_='product-card-brand')

pañales = list()

for i in ps:
    pañales.append(i.text)


#Tipo = tp

tp = soup.find_all('div', class_='product-card-name')

tipo = list()

for i in tp:
    tipo.append(i.text)


#Mejorprecio = mp

mp = soup.find_all('span', class_='best-price')

mejorprecio = list()

for i in mp:
    mejorprecio.append(i.text)


df = pd.DataFrame({'Nombre': pañales, 'Descripcion': tipo, 'Precio': mejorprecio}, index=list(range(1, 43)))

df.to_csv('Comparacion_Farmacity_Pañales.csv')