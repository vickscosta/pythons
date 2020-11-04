import random
import copy
from cartas_src import cartas_class

PARTIDAS=['Vazas','Copas',"Damas","Homens","King","2 ultimas"]

class jogo_class():

    def __init__(self):
        self.ronda=0
        self.partida=0
        self.nome_partida=None
        self.ordem=None
        self.primeiro_a_jogar=None
        self.cartas_que_ja_sairam=None

    def actualisa_ordem(self):
        if self.ronda==0 and self.partida==0:
            self.primeiro_a_jogar=random.randint(0,3)
        
        if self.primeiro_a_jogar==0:
            self.ordem=[0,1,2,3]
        elif self.primeiro_a_jogar==1:
            self.ordem=[1,2,3,0]
        elif self.primeiro_a_jogar==2:
            self.ordem=[2,3,0,1]
        elif self.primeiro_a_jogar==3:
            self.ordem=[3,0,1,2]

    def prepara_partida(self,baralho_,jogador):
        self.partida = self.partida if self.partida==0 else self.partida+1
        self.nome_partida=PARTIDAS[self.partida]
        print('\n***',self.nome_partida,'***')
        
        baralho=copy.deepcopy(baralho_)
        baralho.baralha()
        [j.apanha_mao(cartas_class(baralho.distribui_13_cartas())) for j in jogador]
        
        self.cartas_que_ja_sairam=cartas_class()

    def começa_partida(self,jogador):
        
        for ronda in range(13):
           
            self.ronda=ronda
            vaza=cartas_class()
            print('\nRonda',self.ronda+1)
            self.actualisa_ordem()
            primeira_carta_jogada=None
                      
            for posicao in range(4):
          
                jogador[self.ordem[posicao]].calcula_cartas_candidatas(primeira_carta_jogada)
                carta_jogada=jogador[self.ordem[posicao]].joga_carta(self.nome_partida,primeira_carta_jogada)
                jogador[self.ordem[posicao]].retira_carta(carta_jogada)
                vaza.junta_cartas(carta_jogada)
                print('O jogador',self.ordem[posicao],'jogou a carta',carta_jogada['carta'])

                if primeira_carta_jogada is None:
                    primeira_carta_jogada=carta_jogada

            self.cartas_que_ja_sairam.junta_cartas(vaza)
            vencedor_vaza=self.ordem[self.calcula_quem_ganhou_a_vaza(primeira_carta_jogada,vaza)]
            jogador[vencedor_vaza].actualisa_pontos(quantidade=1,partida=self.nome_partida)

            # self.actualisa_jogo()

    def calcula_quem_ganhou_a_vaza(self,puxada,vaza):
        
        best=puxada
        best_idx=None
        for idx,carta in enumerate(vaza.saco):
            if carta['naipe']==puxada['naipe']:
                if carta['valor']>=best['valor']:
                    best=carta
                    best_idx=idx
        return best_idx