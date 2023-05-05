import requests
from bs4 import BeautifulSoup as bs
import re

def get_slug(slugtorneio, nometime):
    
    html = requests.get(f'https://www.thepunterspage.com/kickform/{slugtorneio}-matchday-tips/').text
    sp = bs(html, 'html.parser')
    pattern = re.compile(nometime)
    href = sp.find('a', attrs={'title':pattern}) 
    slug = href['href']
    return slug

def get_probs(slug):
    html = requests.get(f'https://www.thepunterspage.com{slug}').text
    soup = bs(html,'html.parser')

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

#def get_ocorrencies(slug):
slug = '/kickform/fc-schalke-04-vs-fsv-mainz-05/'
html = requests.get(f'https://www.thepunterspage.com{slug}').text
soup = bs(html,'html.parser')
link_tables_tags = soup.find_all('div', class_='col-lg-4 col-md-6')
link_tables =[]
for i in link_tables_tags:
    iframe = i.find('iframe')
    link = iframe['src']
    link = link.split('?')
    link[0] = link[0].replace('https://www.adamchoi.co.uk/widget.html#/thepunterspage/', '')
    link1 = link[1].split('&')
    final_link = f'https://www.adamchoi.co.uk/scripts/data/json/scripts/getStatsTablesSecure.php?clflc=abc&stat={link[0]}&numMatches=All&minPercent=-1&getFixtures=false&{link1[0]}&matchesType=All&minPlayed=0&{link1[1]}'
    link_tables.append(final_link)

print(link_tables)
# for i in link_tables:
#     html = requests.get(i)
#     soup = bs(html, 'html.parser').text

