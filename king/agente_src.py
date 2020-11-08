import random
from cartas_src import baralho_class

baralho_agente=baralho_class()

class agente_class():

    def __init__(self,tipo):
        self.tipo=tipo
        return

    def escolhe_carta(self,mao,cartas_candidatas,balda,vaza,nome_partida,primeira_carta_jogada=None):

        if self.tipo=='Humano':
            escolha_ok=False
            escolha_cand_ok=False
            while escolha_ok==False or escolha_cand_ok==False:
                print('\nEscolha uma carta\n',mao.mostra_cartas())
                carta_manual=input('->')
                carta_manual_completa,escolha_ok=self.calcula_carta_jogada_manual(carta_manual)
                if carta_manual_completa in cartas_candidatas.saco:
                    escolha_cand_ok=True
                    carta_escolhida=carta_manual_completa
                else:
                    print('Carta ilegal')
        
        elif self.tipo=='Medricas':
            if balda==False:
                carta_escolhida=self.calcula_maior_carta_menor_mesa(cartas_candidatas.saco,vaza)
            else:
                if nome_partida=='Copas' and cartas_candidatas.nb_copas>0:
                    carta_escolhida=self.calcula_maior_carta(cartas_candidatas.copas)
                
                elif nome_partida=='King' and cartas_candidatas.nb_king>0:
                    carta_escolhida=cartas_candidatas.king[0]

                elif nome_partida=='Damas' and cartas_candidatas.nb_damas>0:
                    escolha=random.randint(0,cartas_candidatas.nb_damas-1)
                    carta_escolhida=cartas_candidatas.damas[escolha]
                
                elif nome_partida=='Homens' and cartas_candidatas.nb_homens>0:
                    escolha=random.randint(0,cartas_candidatas.nb_homens-1)
                    carta_escolhida=cartas_candidatas.homens[escolha]
                else:
                    carta_escolhida=self.calcula_maior_carta(cartas_candidatas.saco)

        elif self.tipo=='Burro':
            escolha=random.randint(0,cartas_candidatas.nb-1)
            carta_escolhida=cartas_candidatas.saco[escolha]        
        
        return carta_escolhida
    
    def calcula_carta_jogada_manual(self,carta):

        for carta_baralho in baralho_agente.cartas.saco:
            if carta_baralho['carta']==carta:
                return carta_baralho,True
        return None,False

    def calcula_maior_carta(self,cartas):
        maior_carta=cartas[0]
        for carta in cartas:
            if carta['valor']>=maior_carta['valor']:
                maior_carta=carta
        return maior_carta

    def calcula_menor_carta(self,cartas):
        menor_carta=cartas[-1]
        for carta in cartas:
            if carta['valor']<=menor_carta['valor']:
                menor_carta=carta
        return menor_carta

    def calcula_maior_carta_menor_mesa(self,cartas,vaza):
        melhor_carta=cartas[0]
        if len(vaza.saco)==0:
            return self.calcula_menor_carta(cartas)
        else:
            for carta in cartas:
                for carta_outro_jogador in vaza.saco:
                    if carta['valor']>=melhor_carta['valor'] and carta['valor']<carta_outro_jogador['valor']:
                        melhor_carta=carta
        return melhor_carta