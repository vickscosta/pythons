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
jogador[1]=jogador_class(0,'Burro')
jogador[2]=jogador_class(0,'Normal')
jogador[3]=jogador_class(0,'Medricas')

# 'Humano', 'Medricas', 'Normal', 'Burro', 'Especialista'

def joga_carta_copas(cartas,gajo,balda,lista_cartas,vaza,flag):

    # ESPECIALISTA
    if gajo==1:
        if balda==False:
            carta_escolhida=calcula_maior_carta_menor_mesa_especial(cartas,vaza)            
        else:
            carta_escolhida=calcula_melhor_balda(cartas)

    # CAGADO
    elif gajo==2:
        if balda==False:
            carta_escolhida=cartas[0]
        else:
            carta_escolhida=calcula_maior_carta_copas(cartas)
    
    # NORMAL
    elif gajo==3:
        if balda==False:
            carta_escolhida=calcula_maior_carta_menor_mesa(cartas,vaza)            
        else:
            carta_escolhida=calcula_maior_carta_copas(cartas)

    # HUMANO
    elif gajo==0:
        escolha_ok=False
        escolha_cand_ok=False
        while escolha_ok==False or escolha_cand_ok==False:
            print('\nEscolha uma carta\n',mostra_cartas(jogador[0]))
            carta_manual=input()
            carta_manual_completa,escolha_ok=calcula_carta_jogada_manual(carta_manual,lista_cartas)
            if carta_manual_completa in cartas:
                escolha_cand_ok=True
                carta_escolhida=carta_manual_completa
            else:
                print('Carta Ilegal')

    # ALEATORIO
    else:
        escolha=random.randint(0,len(cartas)-1)
        carta_escolhida=cartas[escolha]
    
    return carta_escolhida

# **************************************************************************************************
def mostra_cartas_dos_jogadores(jogadores):

    for j in jogadores:
        print('P', j.idx,':',j.mao.mostra_cartas())
    return

score_list=[]
NB_JOGOS=1

for nb_jogos_king in range(NB_JOGOS):
    king=jogo_class()
    for j in jogador:
        j.pontos=0
    print('\n*********************************')
    print('*******  JOGO',nb_jogos_king,'*****************')
    print('*********************************')
    
    for game in range(6):

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
    


