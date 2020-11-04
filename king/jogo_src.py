import random
import copy
from cartas_src import cartas_class

PARTIDAS=['Vazas','Copas',"Damas","Homens","King","2 ultimas"]

class jogo_class():

    def __init__(self):
        self.ronda=0
        self.vaza=0
        self.partida=0
        self.nome_partida=None
        self.ordem=self.actualisa_ordem(random.randint(0,3))
        self.primeiro_a_jogar=self.ordem[0]
        self.vencedor_vaza=0

    def actualisa_ordem(self,primeiro_a_jogar):
        if primeiro_a_jogar==0:
            return [0,1,2,3]
        elif primeiro_a_jogar==1:
            return [1,2,3,0]
        elif primeiro_a_jogar==2:
            return [2,3,0,1]
        elif primeiro_a_jogar==3:
            return [3,0,1,2]

    def prepara_partida(self,baralho_,jogador):
        self.partida = self.partida if self.partida==0 else self.partida+1
        self.nome_partida=PARTIDAS[self.partida]
        print('\n***',self.nome_partida,'***')
        
        baralho=copy.deepcopy(baralho_)
        baralho.baralha()
        [j.apanha_mao(cartas_class(baralho.distribui_13_cartas())) for j in jogador]


    def começa_partida(self,jogador):
        
        for ronda in range(13):
           
            # # else:
            # #     ordem=get_order(vencedor_vaza)
            # #     print('\nComeça o jogador',ordem[0])
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