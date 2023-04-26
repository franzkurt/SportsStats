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

def estatisticas(id, torneio, season):
    url = f'https://api.sofascore.com/api/v1/team/{id}/unique-tournament/{torneio}/season/{season}/statistics/overall'
    html = requests.get(url, headers=header)
    json_data = json.loads(html.text)
    statistics = json_data['statistics']
    partidas = statistics['matches']
    gols_favor = statistics['goalsScored']
    gols_contra = statistics['goalsConceded']
    fin_gol = statistics['shotsOnTarget']
    finalizacoes = statistics['shots']
    corners_favor = statistics['corners']
    amarelos = statistics['yellowCards']
    amarelos_adv = statistics['yellowCardsAgainst'] 
    corners_contra = statistics['cornersAgainst']
    impedimentos = statistics['offsides']
    impedimentos_adv = statistics['offsidesAgainst']
    return print(f'{partidas} Partidas jogadas\n{gols_favor / partidas} Média de gols marcados\n{gols_contra / partidas} Média de gols cedidos\n{finalizacoes / partidas} Finalizações por jogo\n{fin_gol / partidas} Chutes a gol por jogo\n'
f'{corners_favor / partidas} Escanteios por jogo\n{corners_contra / partidas} Escanteios cedidos por jogo\n{amarelos / partidas} Cartões amarelos por jogo'
f'\n{amarelos_adv / partidas} Cartões amarelos do adversário por jogo\n{impedimentos / partidas} Impedimentos por jogo\n{impedimentos_adv / partidas} Impedimentos do adversário por jogo')


html = requests.get('https://api.sofascore.com/api/v1/team/30/unique-tournament/17/season/41886/statistics/overall', headers=header)
json_data = json.loads(html.text)
statistics = json_data['statistics']
partidas = statistics['matches']
corners_favor = statistics['corners']
amarelos = statistics['yellowCards']
amarelos_adv = statistics['yellowCardsAgainst'] 
corners_contra = statistics['cornersAgainst']
impedimentos = statistics['offsides']
impedimentos_adv = statistics['offsidesAgainst']
