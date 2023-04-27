import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.soccerstats.com/pmatch.asp?league=italy&stats=215-5-2-2023-lecce-udinese'
html = requests.get(url).text
soup = bs(html, 'html.parser')
tag_h2 = soup.find('h2', string='Corner statistics')
stats = {}
stat = tag_h2.text
empty = tag_h2.next_sibling
tabela = empty.next_sibling
nomes = tabela.find_all('font', {'style':'font-size:13px;font-weight:bold;'})
homename = nomes[0].text
awayname = nomes[1].text
#print(homename, awayname)

empty = tabela.next_sibling
data_table = empty.next_sibling
keys = data_table.find_all('font', {'color' : '#fafafa' })

dados_tags = data_table.find_all('td',{'width' : '13%'} )
name_dados_tags = data_table.find_all('td',{'width' : '48%'})
name_dados = []
dados = []
for i in name_dados_tags:
    x = i.text
    x = x.strip()
    if x == 'Stat':
        continue
    name_dados.append(x)
for i in dados_tags:
    x = i.text
    x = x.strip()
    dados.append(x)

for i in range(4,len(dados),4):
    print(dados[i], dados[i+1],dados[i+2],dados[i+3])
    
print(name_dados)





stats[homename], stats[awayname] = {} , {}
stats[homename][stat], stats[awayname][stat] = {}, {}


