import requests
from bs4 import BeautifulSoup as bs
import re

def get_probs(slugtorneio, nometime):
    
    html = requests.get(f'https://www.thepunterspage.com/kickform/{slugtorneio}-matchday-tips/').text
    sp = bs(html, 'html.parser')
    pattern = re.compile(nometime)
    href = sp.find('a', attrs={'title':pattern})
    slug = href['href']

    html = requests.get(f'https://www.thepunterspage.com{slug}').text

    soup = bs(html,'html.parser')

    names = soup.find_all('div', class_='card_headline')
    insides = soup.find_all('div', class_='inside')
    insides = insides[:4]
    insides1 = insides[0], insides[-1]
    insides2 = insides[1], insides[2]
    for i in insides1 :
        valores = i.find_all(string = True)
        lista_valor = [p.strip() for p in valores]
        lista_valor1 = list(filter(bool, lista_valor))
        print('\n', lista_valor1[0])
        lista_valor1 = lista_valor1[1:]
        
        for p in range(0,len(lista_valor1),3):
            print(lista_valor1[p], lista_valor1[p+1], lista_valor1[p+2])
    for i in insides2:
        valores = i.find_all(string = True)
        lista_valor = [p.strip() for p in valores]        
        lista_valor1 = list(filter(bool, lista_valor))
        print('\n',lista_valor1[0])
        lista_valor1 = lista_valor1[1:]
        if len(lista_valor1)< 10:
            for p in range(0,len(lista_valor1),2):
                print(lista_valor1[p], lista_valor1[p+1])
        else:
            for p in range(0,len(lista_valor1),6):
                print(lista_valor1[p+4],':' ,lista_valor1[p], lista_valor1[p+1])
                print(lista_valor1[p+5],':', lista_valor1[p+2], lista_valor1[p+3])
        
    