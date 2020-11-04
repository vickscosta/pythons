# import random
import copy
from cartas_src import cartas_class

class jogo_class():

    def __init__(self):
        pass

    def Começa_partida(self,baralho_,jogador):
        self.ronda=1
        baralho=copy.deepcopy(baralho_)
        baralho.baralha()

        for _ in range(4):
            mao=cartas_class(baralho.distribui_13_cartas())
            pass


        #     jogador[j].junta_carta(self.cartas_distib.pop())
        #     jogador[j]=ordena_cartas()
        # mostra_cartas_dos_jogadores(jogador)

        # return