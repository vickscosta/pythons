import random
from cartas_src import baralho_class

baralho_agente=baralho_class()

class agente_class():

    def __init__(self,tipo):
        self.tipo=tipo
        return

    def escolhe_carta(self,mao,cartas_candidatas,nome_partida,primeira_carta_jogada=None):

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

        elif self.tipo=='Burro':
            escolha=random.randint(0,cartas_candidatas.nb-1)
            carta_escolhida=cartas_candidatas.saco[escolha]        
        
        return carta_escolhida
    
    def calcula_carta_jogada_manual(self,carta):

        for carta_baralho in baralho_agente.cartas.saco:
            if carta_baralho['carta']==carta:
                return carta_baralho,True
        return None,False