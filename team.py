import requests
import json
from bs4 import BeautifulSoup as bs


header = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.sofascore.com',
    'referer': 'https://www.sofascore.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
url = 'https://api.sofascore.com/api/v1/team/3/unique-tournament/17/season/41886/statistics/overall'
html = requests.get(url, headers=header)
json_data = json.loads(html.text)
estatisticas = json_data['statistics']
partidas = estatisticas['matches']
corners = estatisticas['corners']
amarelos = estatisticas['yellowCards']
print(f'{corners / partidas} Escanteios por jogo, {amarelos / partidas} Cartões amarelos por jogo')