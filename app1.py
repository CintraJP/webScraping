import requests
from bs4 import BeautifulSoup
import pandas as pd
 
 
texto_carro = []
modelo = []
imagem = []
informacoes = []
marcaCarro = []

url_post = 'http://127.0.0.1:8000/app/cars/'


def scraping_cars(marca: str):
    cars_url = f'https://www.autoevolution.com/{marca}'
    browsers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    page = requests.get(cars_url, headers = browsers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    marcador = soup.find_all('div', class_ = 'col2width bcol-white fl')

    nome_carros = [i.find('a').get('href') for i in marcador] 
    for i in range (len(nome_carros)):
        url_especifica = nome_carros[i]
        page_especifica = requests.get(url_especifica, headers = browsers)

        soup2 = BeautifulSoup(page_especifica.content, 'html.parser')

        loc_infos = soup2.find('div', class_= 'padsides_20i newstext mgbot_20 fsz14')
        
        
        achar_texto = soup2.find_all('div', class_='txt newstext')
        
        
        loc_modelo = soup2.find_all('span', class_ = 'col-red')
        
        
        img = soup2.find_all('div', class_= 'col1width fl')
        loc_imagem = [i.find('img').get('src') for i in img]
        

        for x in range(len(achar_texto)):
            texto_carro.insert(x, achar_texto[x].text )
            modelo.insert(x, loc_modelo[x].text)
            imagem.insert(x, loc_imagem[x])
            informacoes.insert(x, loc_infos.text)
            marcaCarro.insert(x, marca)
    
    
    for i in range(len(marcaCarro)):
        data = {
        "brand": f'{marcaCarro[i]}',
        "model": f'{modelo[i]}',
        "info": f'{informacoes[i]}',
        "text": f'{texto_carro[i]}',
        "img": f'{imagem[i]}'
        }
        r = requests.post(url_post, data = data)
        print(r)


print('oi')

















