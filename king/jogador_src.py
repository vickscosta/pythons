import random
from cartas_src import cartas_class

class jogador_class():

    def __init__(self,idx):
        self.idx=idx
        self.agente='Humano'
        self.pontos_partida=0
        self.pontos=0
        return
        
    def apanha_mao(self,mao):
        self.mao=mao
        return

    def calcula_cartas_candidatas(self,nome_partida,primeira_carta_jogada=None):
        
        self.cartas_candidatas=cartas_class(None)
        self.balda=False
    
        for carta in self.mao.saco:
            #primeiro a jogar
            if primeira_carta_jogada is None:
                #não se pode puxar copas
                if nome_partida=='Copas' or nome_partida=='King':
                    #se só tiver copas
                    if self.mao.nb-self.mao.nb_copas==0:
                        self.cartas_candidatas.junta_cartas(carta)
                    elif carta['naipe'] != 'C':
                        self.cartas_candidatas.junta_cartas(carta)
                else:
                    self.cartas_candidatas.junta_cartas(carta)
            #assistir a uma puxada
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
        self.mao.actualiza_saco()
        return

    def inicializa_pontos(self):
        self.pontos_partida=0
        return

    def actualiza_pontos_ronda(self,vaza,partida,ronda):
        
        if partida=='Vazas':
            self.pontos_partida+=20
        
        elif partida=='Copas':
            self.pontos_partida+=20*vaza.nb_copas
        
        elif partida=='Damas':
            damas=0
            for c in vaza.saco:
                if c['valor']==12:
                    damas+=1
            self.pontos_partida+=50*damas
        
        elif partida=='Homens':
            homens=0
            for c in vaza.saco:
                if c['valor']==11 or c['valor']==13:
                    homens+=1
            self.pontos_partida+=30*homens
        
        elif partida=='King':
            for c in vaza.saco:
                if c['carta']=='KC':
                    self.pontos_partida=160
        
        elif partida=='2 ultimas':
            if ronda==11 or ronda==12:
                self.pontos_partida+=90
        return

    def actualiza_pontos_total(self):
        self.pontos+=self.pontos_partida
        return