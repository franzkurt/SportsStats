import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.soccerstats.com/pmatch.asp?league=england&stats=563-10-18-2023-nottm-forest-brighton'
html = requests.get(url).text
soup = bs(html, 'html.parser')
tag_h2 = soup.find('h2', string='Corner statistics')
empty = tag_h2.next_sibling
tabela = empty.next_sibling
nomes = tabela.find_all('font', {'style':'font-size:13px;font-weight:bold;'})
homename = nomes[0].text
awayname = nomes[1].text
print(homename, awayname)

empty = tabela.next_sibling
data_table = empty.next_sibling
diferenca = data_table.find_all('font', {'color' : '#fafafa' })
print(diferenca[0].text)

stats = { }
stats[homename], stats[awayname] = {} , {}
