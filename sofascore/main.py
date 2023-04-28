import event
import team
from match import info_soccerstats

link = input('Informe a partida Sofascore: ')
ids = event.informar_partida(link)
# link = input('Informe a partida SoccerStats: ')
# info_soccerstats(link)

id_partida, id_season, id_torneio = ids[0], ids[1], ids[2]

dados = event.dados_evento(id_partida)

torneio, hometeam, awayteam, homeslug, homeid, awayslug, awayid = dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]

sequencias = event.sequencias(id_partida)

for i in sequencias[0]:
    nome_time = i['team']
    if nome_time == 'away':
        nome_time = awayteam
    if nome_time == 'home':
        nome_time = hometeam
    print(nome_time, i['name'],i['value'])
print('-' * 10,'Head 2 Head', '-' * 10)

for i in sequencias[1]:
    nome_time = i['team']
    if nome_time == 'away':
        nome_time = awayteam
    if nome_time == 'home':
        nome_time = hometeam
    print(nome_time, i['name'],i['value'])

print('-' * 10,hometeam,'-' * 10)
team.estatisticas(homeid,id_torneio,id_season)
print('-' * 10,awayteam,'-' * 10)
team.estatisticas(awayid,id_torneio,id_season)

event.situacao(id_partida)

print('-' * 20)
team.player_stats(homeid,id_torneio,id_season)
print('-' * 20)
team.player_stats(awayid,id_torneio,id_season)