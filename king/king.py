# import random
# import copy

VER_CARTAS_AO_INICIO=False

# lista_copas=[('AC',14,'C'),('2C',2,'C'),('3C',3,'C'),('4C',4,'C'),('5C',5,'C'),('6C',6,'C'),('7C',7,'C'),('8C',8,'C'),('9C',9,'C'),('10C',10,'C'),('VC',11,'C'),('DC',12,'C'),('KC',13,'C')]
# lista_paus=[('AP',14,'P'),('2P',2,'P'),('3P',3,'P'),('4P',4,'P'),('5P',5,'P'),('6P',6,'P'),('7P',7,'P'),('8P',8,'P'),('9P',9,'P'),('10P',10,'P'),('VP',11,'P'),('DP',12,'P'),('KP',13,'P')]
# lista_espadas=[('AE',14,'E'),('2E',2,'E'),('3E',3,'E'),('4E',4,'E'),('5E',5,'E'),('6E',6,'E'),('7E',7,'E'),('8E',8,'E'),('9E',9,'E'),('10E',10,'E'),('VE',11,'E'),('DE',12,'E'),('KE',13,'E')]
# lista_ouros=[('AO',14,'O'),('2O',2,'O'),('3O',3,'O'),('4O',4,'O'),('5O',5,'O'),('6O',6,'O'),('7O',7,'O'),('8O',8,'O'),('9O',9,'O'),('10O',10,'O'),('VO',11,'O'),('DO',12,'O'),('KO',13,'O')]

# _copas=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_copas]
# _paus=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_paus]
# _espadas=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_espadas]
# _ouros=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_ouros]
# _baralho=_copas+_paus+_espadas+_ouros

from cartas_src import cartas_class
from cartas_src import baralho_class
from jogo_src import jogo_class
from agente_src import agente_class
from jogador_src import jogador_class

baralho=baralho_class()

king=jogo_class()
# jogador=[jogador_class(idx) for idx in range(4)]
jogador=[None for _ in range(4)]
jogador[0]=jogador_class(0,'Burro')
jogador[1]=jogador_class(1,'Burro')
jogador[2]=jogador_class(2,'Medricas')
jogador[3]=jogador_class(3,'Medricas')

def calcula_maior_carta_copas(cartas):

    cartas_copas=[]
    for carta in cartas:
        if carta in lista_copas:
            cartas_copas.append(carta)
 
    if len(cartas_copas)>0:
        maior_carta=cartas_copas[0]
        for carta in cartas_copas:
            if carta[1]>=maior_carta[1]:
                maior_carta=carta

    else:
        maior_carta=calcula_maior_carta(cartas)

    return maior_carta

def calcula_maior_carta_menor_mesa_especial(cartas,vaza):

    melhor_carta=cartas[0]
    if len(vaza)==0:
        return melhor_carta
    
    if len(vaza)==3:
        sempre_mau=True
        for carta in cartas:
            for carta_outro_jogador in vaza:
                if carta[1]>=melhor_carta[1] and carta[1]<carta_outro_jogador[1]:
                    melhor_carta=carta
                    sempre_mau=False
        
        if sempre_mau==True:
            for carta in cartas:
                if carta[1]>=melhor_carta[1]:
                    melhor_carta=carta
    else:
        for carta in cartas:
            for carta_outro_jogador in vaza:
                if carta[1]>=melhor_carta[1] and carta[1]<carta_outro_jogador[1]:
                    melhor_carta=carta

    return melhor_carta

def calcula_melhor_balda(cartas):

    melhor_balda=cartas[0]
    NbCartasNaipe=[0,0,0,0]

    for carta in cartas:
        for idx,naipe in enumerate('COPE'):
            if carta[2]==naipe:
                NbCartasNaipe[idx]+=1
    
    min_naipe_nao_nulo=13
    for idx in range(4):
        if NbCartasNaipe[idx]!=0 and NbCartasNaipe[idx]<=min_naipe_nao_nulo:
            min_naipe_nao_nulo=NbCartasNaipe[idx]

    for idx,naipe in enumerate('COPE'):
        for carta in cartas:
            if NbCartasNaipe[idx]==min_naipe_nao_nulo and carta[2]==naipe:
                if carta[1]>melhor_balda[1]:
                    melhor_balda=carta

    return melhor_balda

# def simula_cenario(carta,vaza, cartas_jogadas, mao_jogador,todas_as_cartas,primeira_carta_jogada):

#     i_vaza=copy.deepcopy(vaza)

#     cartas_em_jogo=copy.deepcopy(todas_as_cartas)
#     for carta in cartas_jogadas:
#         cartas_em_jogo.remove(carta)
    
#     for carta in mao_jogador:
#         cartas_em_jogo.remove(carta)

#     for carta in cartas:
#         i_vaza.append(carta)
#         while len(i_vaza)<5:
#             for carta_outros in cartas_em_jogo:
#                 i_vaza.append(carta_outros)
#                 winner=calcula_quem_ganhou_a_vaza(primeira_carta_jogada,_ivaza)
                

def joga_carta_vazas(cartas,gajo,balda,lista_cartas,vaza):

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
            carta_escolhida=calcula_maior_carta(cartas)
    
    # NORMAL
    elif gajo==3:
        if balda==False:
            carta_escolhida=calcula_maior_carta_menor_mesa(cartas,vaza)            
        else:
            carta_escolhida=calcula_melhor_balda(cartas)

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
                print('Carta ilegal')

    # ALEATORIO
    else:
        escolha=random.randint(0,len(cartas)-1)
        carta_escolhida=cartas[escolha]
    
    return carta_escolhida

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
for game in range(6):

    king.prepara_partida(baralho.cartas,jogador)

    if VER_CARTAS_AO_INICIO:
        mostra_cartas_dos_jogadores(jogador) 

    king.começa_partida(jogador)

    print('\n')
    print(king.nome_partida, [j.pontos_partida for j in jogador])
    print('Total',[j.pontos for j in jogador])

print('verificação',sum([j.pontos for j in jogador]))

    # for ronda in range(13):
    #     print('\nRONDA:',king.ronda+1)
    #     print('\nComeça o jogador',king.primeiro_a_jogar)
        
        # else:
        #     ordem=get_order(vencedor_vaza)
        #     print('\nComeça o jogador',ordem[0])
        # for posicao in range(4):
        #     cartas_candidatas,balda=calcula_cartas_candidatas(jogador[ordem[posicao]],primeira_carta_jogada)
        #     carta_jogada=joga_carta_vazas(cartas_candidatas,ordem[posicao],balda,lista_cartas,vaza)
        #     jogador[ordem[posicao]].remove(carta_jogada)
        #     vaza.append(carta_jogada)
        #     print('O jogador',ordem[posicao],'jogou a carta',carta_jogada[0])

        #     if len(primeira_carta_jogada)==0:
        #         primeira_carta_jogada=carta_jogada

        # vencedor_vaza=ordem[calcula_quem_ganhou_a_vaza(primeira_carta_jogada,vaza)]
        # pontos=actualiza_pontos(pontos,vencedor_vaza)

        # ipdateking


    
#     print('\nPontos vazas',pontos,'\n')
#     pontos_vazas=copy.deepcopy(pontos)

#     print('***************** NAO FAZER COPAS *****************')
#     ronda, jogador, pontos = init_game(lista_cartas)
#     copas_flag=False

#     for ronda in range(13):
#         print('\nRONDA:',ronda+1)
#         primeira_carta_jogada=[]
#         vaza=[]
#         if ronda==0:
#             ordem=get_order()
#             print('\nComeça o jogador',ordem[0])
#         else:
#             ordem=get_order(vencedor_vaza)
#             print('\nComeça o jogador',ordem[0])
#         for posicao in range(4):
#             cartas_candidatas,balda=calcula_cartas_candidatas_copas(jogador[ordem[posicao]],primeira_carta_jogada,copas_flag)
#             carta_jogada=joga_carta_copas(cartas_candidatas,ordem[posicao],balda,lista_cartas,vaza,copas_flag)
#             jogador[ordem[posicao]].remove(carta_jogada)
#             vaza.append(carta_jogada)
#             print('O jogador',ordem[posicao],'jogou a carta',carta_jogada[0])

#             if carta_jogada in lista_copas:
#                copas_flag=True
           
#             if len(primeira_carta_jogada)==0:
#                 primeira_carta_jogada=carta_jogada

#         vencedor_vaza=ordem[calcula_quem_ganhou_a_vaza(primeira_carta_jogada,vaza)]
#         pontos=actualiza_pontos_copas(pontos,vencedor_vaza,vaza)
    
#     pontos_copas=copy.deepcopy(pontos)
#     print('\nPontos Copas',pontos)
    
#     total_pontos=[0,0,0,0]
#     for i in range(4):
#         total_pontos[i]=pontos_vazas[i]+pontos_copas[i]

#     print('\nTotal pontos',total_pontos)



#     score_list.append(pontos)

# avg_score=[0,0,0,0]
# sum_score=[0,0,0,0]
# for score in score_list:
#     for idx,j in enumerate(score):
#         sum_score[idx]+=j

# for i in range(4):
#     avg_score[i]=sum_score[i]/len(score_list)

# #print('\n',score_list)   
# print('\n',avg_score)
    


