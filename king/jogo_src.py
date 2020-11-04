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
        [j.apanha_mao(cartas_class(baralho.distribui_13_cartas())) for j in jogador]

        # for i in range(4):
            # mao=cartas_class(baralho.distribui_13_cartas())
            # jogador[i].apanha_mao(cartas_class(baralho.distribui_13_cartas()))