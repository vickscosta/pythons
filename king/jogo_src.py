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
        self.cartas_que_ja_sairam=None
        self.primeiro_jogador=random.randint(0,3)

    def actualiza_ordem(self):
        if self.ronda==0:
            self.primeiro_a_jogar_ronda=(self.primeiro_jogador+self.partida)%4
        self.ordem=[(self.primeiro_a_jogar_ronda+i)%4 for i in range(4)]
        return

    def prepara_partida(self,baralho_,jogador):
        self.nome_partida=PARTIDAS[self.partida]
        print('\n***',self.nome_partida,'***')
        
        baralho=copy.deepcopy(baralho_)
        baralho.baralha()
        [j.apanha_mao(cartas_class(baralho.distribui_13_cartas())) for j in jogador]
        [j.inicializa_pontos() for j in jogador]
        
        self.cartas_que_ja_sairam=cartas_class()
        return

    def começa_partida(self,jogador):
        
        for ronda in range(13):
           
            self.ronda=ronda
            vaza=cartas_class()
            print('\nRonda',self.ronda+1)
            self.actualiza_ordem()
            primeira_carta_jogada=None
   
            for posicao in range(4):
          
                jogador[self.ordem[posicao]].calcula_cartas_candidatas(self.nome_partida,primeira_carta_jogada)
                carta_jogada=jogador[self.ordem[posicao]].joga_carta(self.nome_partida,primeira_carta_jogada)
                jogador[self.ordem[posicao]].retira_carta(carta_jogada)
                vaza.junta_cartas(carta_jogada)
                print('O jogador',self.ordem[posicao],'jogou a carta',carta_jogada['carta'])

                if primeira_carta_jogada is None:
                    primeira_carta_jogada=carta_jogada

            self.cartas_que_ja_sairam.junta_cartas(vaza)
            vencedor_vaza=self.ordem[self.calcula_quem_ganhou_a_vaza(primeira_carta_jogada,vaza)]
            self.primeiro_a_jogar_ronda=vencedor_vaza
            jogador[vencedor_vaza].actualiza_pontos_ronda(vaza,self.nome_partida,self.ronda)

        [j.actualiza_pontos_total() for j in jogador]
        self.partida+=1    
        return


    def calcula_quem_ganhou_a_vaza(self,puxada,vaza):
        
        best=puxada
        best_idx=None
        for idx,carta in enumerate(vaza.saco):
            if carta['naipe']==puxada['naipe']:
                if carta['valor']>=best['valor']:
                    best=carta
                    best_idx=idx
        return best_idx