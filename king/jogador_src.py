import random
from cartas_src import cartas_class

class jogador_class():

    def __init__(self,idx):
        self.idx=idx
        self.agente='Humano'
        self.pontos=0
        return
        
    def apanha_mao(self,mao):
        self.mao=mao
        return

    def calcula_cartas_candidatas(self,primeira_carta_jogada=None):
        
        self.cartas_candidatas=cartas_class(None)
        self.balda=False
    
        for carta in self.mao.saco:
            if primeira_carta_jogada is None:
                self.cartas_candidatas.junta_cartas(carta)
            elif carta['naipe'] == primeira_carta_jogada['naipe']:
                self.cartas_candidatas.junta_cartas(carta)

        #caso das baldas
        if self.cartas_candidatas.nb==0:
            self.cartas_candidatas=self.mao
            self.balda=True
        return

    def joga_carta(self,nome_partida,primeira_carta_jogada=None):
        escolha=random.randint(0,self.cartas_candidatas.nb-1)
        carta_escolhida=self.cartas_candidatas.saco[escolha]
        return carta_escolhida

    def retira_carta(self,carta):
        self.mao.saco.remove(carta)
        self.mao.actualisa_saco()
        return

    def actualisa_pontos(self,quantidade,partida):
        if partida=='Vazas':
            self.pontos+=20*quantidade
        return