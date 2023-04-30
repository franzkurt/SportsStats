import requests
import json
from bs4 import BeautifulSoup as bs
from event import informar_partida

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

def estatisticas(ide, torneio, season):
    url = f'https://api.sofascore.com/api/v1/team/{ide}/unique-tournament/{torneio}/season/{season}/statistics/overall'
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
f'{corners_favor / partidas} Escanteios por jogo\n{corners_contra / partidas} Escanteios cedidos por jogo\n{(corners_favor / partidas) + (corners_contra / partidas)} Escanteios na partida\n{amarelos / partidas} Cartões amarelos por jogo'
f'\n{amarelos_adv / partidas} Cartões amarelos do adversário por jogo\n{impedimentos / partidas} Impedimentos por jogo\n{impedimentos_adv / partidas} Impedimentos do adversário por jogo')

def player_stats(ide, torneio, season):
    url = f'https://api.sofascore.com/api/v1/team/{ide}/unique-tournament/{torneio}/season/{season}/top-players/overall'
    html = requests.get(url, headers=header)
    json_data = json.loads(html.text)
    keys = json_data['topPlayers']

    for i in keys:
        for p in keys[i]:
            print(p['player']['name'], p['statistics'])
                

def last_games(ide, name):
    url = f'https://api.sofascore.com/api/v1/team/{ide}/events/last/0'
    html = requests.get(url, headers=header)
    json_data = json.loads(html.text)
    keys = json_data['events']
    gols_primeiro_soma, gols_soma, escanteios_soma, amarelos_soma, partidas_soma, chutes_soma = 0, 0 ,0 ,0 ,0, 0

    for i in keys:
        nome_torneio = i['tournament']['name']
        slug, custom_id = i['slug'], i['customId']
        time_casa = i['homeTeam']['name']
        time_away = i['awayTeam']['name']
        try:
            gols_casa = i['homeScore']['display']
            gols_away = i['awayScore']['display']
            gols_casa_tempo = i['homeScore']['period1']
            gols_away_tempo = i['awayScore']['period1']
        except:
            continue
        id_antigas = informar_partida(f'https://www.sofascore.com/{slug}/{custom_id}')
        url_antiga = f'https://api.sofascore.com/api/v1/event/{id_antigas[0]}/statistics'
        html = requests.get(url_antiga, headers=header)
        json_data_antiga = json.loads(html.text)
        try:
            stats = json_data_antiga['statistics']
        except:
            continue
        print('/' * 20)
        print(nome_torneio,'\n', time_casa, ':', gols_casa, time_away, ':', gols_away, '\n','Gols primeiro tempo:', time_casa, gols_casa_tempo,' - ', time_away, gols_away_tempo )
        for x in stats[0]['groups']:
            for y in x['statisticsItems']:
                if y['name'] == 'Corner kicks' or y['name'] == 'Yellow cards' or y['name'] == 'Total shots':
                    print (y['name'],'-' ,time_casa,':', y['home'], time_away,':', y['away'])
                    if time_casa == name:
                        if y['name'] == 'Corner kicks':
                            escanteios_soma += int(y['home'])
                        elif y['name'] == 'Yellow cards':
                            amarelos_soma += int(y['home'])
                        elif y['name'] == 'Total shots':
                            chutes_soma += int(y['home'])
                    else:
                        if y['name'] == 'Corner kicks':
                            escanteios_soma += int(y['away'])
                        elif y['name'] == 'Yellow cards':
                            amarelos_soma += int(y['away'])
                        elif y['name'] == 'Total shots':
                            chutes_soma += int(y['away'])
                else:
                    continue
        print('escanteios',escanteios_soma,'amarelos', amarelos_soma,'chutes,', chutes_soma)
   

   
   