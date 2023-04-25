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

def informar_partida(url):

    html = requests.get(url, headers=header).text
    soup = bs(html, 'html.parser')
    nextdata = soup.find('script', id='__NEXT_DATA__').string
    json_data = json.loads(nextdata)
    num_event = json_data['props']['pageProps']['event']['id']
    return num_event


def dados_evento(num):
    url = f'https://api.sofascore.com/api/v1/event/{num}'
    html = requests.get(url, headers=header)
    json_data = json.loads(html.text)
    event = json_data['event']
    torneio = event['tournament']['name']
    homeinfo = event['homeTeam']
    awayinfo = event['awayTeam']
    homename = homeinfo['name']
    awayname = awayinfo['name']
    homeslug = homeinfo['slug']
    homeid = homeinfo['id']
    awayslug = awayinfo['slug']
    awayid = awayinfo['id'] 
    return torneio, homename, awayname, homeslug, homeid, awayslug, awayid

def sequencias(num):
    url =f'https://api.sofascore.com/api/v1/event/{num}/team-streaks'
    html = requests.get(url,headers=header)
    json_data = json.loads(html.text)
    general = json_data['general']
    head2head = json_data['head2head']
    return general,head2head
