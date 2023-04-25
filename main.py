import event


dados = (event.dados_evento(event.informar_partida('https://www.sofascore.com/gremio-abc/BtcsNLi')))

torneio, hometeam, awayteam, homeslug, homeid, awayslug, awayid = dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]

sequencias = event.sequencias(event.informar_partida('https://www.sofascore.com/gremio-abc/BtcsNLi'))

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