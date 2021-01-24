from cartas_src import cartas_class
from cartas_src import baralho_class
from jogo_src import jogo_class
from agente_src import agente_class
from jogador_src import jogador_class


VER_CARTAS_AO_INICIO=False

baralho=baralho_class()

# jogador=[jogador_class(idx) for idx in range(4)]
jogador=[None for _ in range(4)]
jogador[0]=jogador_class(0,'Especialista')
jogador[1]=jogador_class(0,'Normal')
jogador[2]=jogador_class(0,'Medricas')
jogador[3]=jogador_class(0,'Humano')

# 'Humano', 'Medricas', 'Normal', 'Burro', 'Especialista'

def mostra_cartas_dos_jogadores(jogadores):

    for j in jogadores:
        print('P', j.idx,':',j.mao.mostra_cartas())
    return

score_list=[]
NB_JOGOS=1000

for nb_jogos_king in range(NB_JOGOS):
    king=jogo_class()
    for j in jogador:
        j.pontos=0
    print('\n*********************************')
    print('*******  JOGO',nb_jogos_king,'*****************')
    print('*********************************')
    
    for game in range(2):

        king.prepara_partida(baralho.cartas,jogador)

        if VER_CARTAS_AO_INICIO:
            mostra_cartas_dos_jogadores(jogador) 

        king.começa_partida(jogador)

        print('\n')
        print(king.nome_partida, [j.pontos_partida for j in jogador])
        print('Total',[j.pontos for j in jogador])
    
    score_list.append([j.pontos for j in jogador])

# print('\n',score_list)    

avg_score=[0,0,0,0]
sum_score=[0,0,0,0]
for score in score_list:
    for idx,j in enumerate(score):
        sum_score[idx]+=j

for i in range(4):
    avg_score[i]=sum_score[i]/len(score_list)

#print('\n',score_list)   
print('\n',avg_score)
    


