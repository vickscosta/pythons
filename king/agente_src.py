import random
import copy
from cartas_src import baralho_class
from cartas_src import cartas_class

baralho_agente=baralho_class()

class agente_class():

    def __init__(self,tipo):
        self.tipo=tipo
        return

    def escolhe_carta(self,mao,cartas_candidatas,balda,vaza,nome_partida,cartas_que_ja_sairam,primeira_carta_jogada=None):

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

        elif self.tipo=='Normal':
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
                    carta_escolhida=self.calcula_melhor_balda(cartas_candidatas)

        elif self.tipo=='Especialista':
            if balda==False:
                carta_escolhida=self.calcula_maior_carta_menor_mesa_especial(cartas_candidatas,vaza,cartas_que_ja_sairam,nome_partida)
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
                    carta_escolhida=self.calcula_melhor_balda_especial(cartas_candidatas,vaza,cartas_que_ja_sairam)

        elif self.tipo=='Burro':
            if balda==True and nome_partida=='King' and cartas_candidatas.nb_king>0:
                carta_escolhida=cartas_candidatas.king[0]
            else:
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

    def calcula_melhor_balda(self,cartas):
        melhor_balda=cartas.saco[0]
        nb_min_naipe_nao_nulo=13
        
        for naipe in [cartas.copas, cartas.espadas, cartas.ouros, cartas.paus]:
            if len(naipe)>0 and len(naipe)<=nb_min_naipe_nao_nulo:
                nb_min_naipe_nao_nulo=len(naipe)
                min_naipe=naipe
        for carta in cartas.saco:
            if carta in min_naipe:
                if carta['valor']>melhor_balda['valor']:
                    melhor_balda=carta
        return melhor_balda

    def calcula_melhor_balda_especial(self,cartas,vaza,cartas_que_ja_sairam):
        melhor_balda=None
        # nb_min_naipe_nao_nulo=13
        
        cartas_que_ainda_nao_sairam=self.calcula_cartas_que_ainda_nao_sairam(cartas,cartas_que_ja_sairam,vaza)

        melhor_naipe=None
        melhor_max=0
        melhor_balda=None

        probabilidade_ganho_por_naipe=self.calcula_prob_de_victoria_por_naipe(cartas,cartas_que_ainda_nao_sairam)

        for idx,c in enumerate(probabilidade_ganho_por_naipe):
            if c>melhor_max and c!=150:
                melhor_max=c
                melhor_naipe=idx

        if melhor_naipe==0:
            if cartas.nb_paus>0:
                melhor_balda=cartas.paus[-1]
        elif melhor_naipe==1:
            if cartas.nb_espadas>0:
                melhor_balda=cartas.espadas[-1]
        elif melhor_naipe==2:
            if cartas.nb_ouros>0:
                melhor_balda=cartas.ouros[-1]
        elif melhor_naipe==3:
            if cartas.nb_copas>0:
                melhor_balda=cartas.copas[-1]
        
        if melhor_balda is None:
            melhor_balda=self.calcula_maior_carta(cartas.saco)
        return melhor_balda

    def calcula_maior_carta_menor_mesa_especial(self,cartas,vaza,cartas_que_ja_sairam,nome_partida):
        melhor_carta=cartas.saco[0]
        if len(vaza.saco)==0:
            melhor_carta=self.calcula_melhor_puxada(cartas,cartas_que_ja_sairam,nome_partida)
            return melhor_carta
        
        sempre_mau=True
        for carta in cartas.saco:
            for carta_outro_jogador in vaza.saco:
                if carta['valor']>=melhor_carta['valor'] and carta['valor']<carta_outro_jogador['valor']:
                    melhor_carta=carta
                    sempre_mau=False
        
        if sempre_mau==True and len(vaza.saco)==3:
            melhor_carta=self.calcula_maior_carta(cartas.saco)

        return melhor_carta

    def calcula_melhor_puxada(self,cartas,cartas_que_ja_sairam,nome_partida):
        
        cartas_que_ainda_nao_sairam=self.calcula_cartas_que_ainda_nao_sairam(cartas,cartas_que_ja_sairam)
        
        melhor_naipe=None
        melhor_min=200
        melhor_puxada=None

        probabilidade_ganho_por_naipe=self.calcula_prob_de_victoria_por_naipe(cartas,cartas_que_ainda_nao_sairam)

        for idx,c in enumerate(probabilidade_ganho_por_naipe):
            if c<melhor_min:
                melhor_min=c
                melhor_naipe=idx

        if nome_partida=='Vazas':

            if melhor_naipe==0:
                if cartas.nb_paus>0:
                    melhor_puxada=cartas.paus[0]
            elif melhor_naipe==1:
                if cartas.nb_espadas>0:
                    melhor_puxada=cartas.espadas[0]
            elif melhor_naipe==2:
                if cartas.nb_ouros>0:
                    melhor_puxada=cartas.ouros[0]
            elif melhor_naipe==3:
                if cartas.nb_copas>0:
                    melhor_puxada=cartas.copas[0]
            
            if melhor_puxada is None:
                melhor_puxada=self.calcula_menor_carta(cartas.saco)
        
        elif nome_partida=='Copas': # isto não esta bom
            melhor_puxada=self.calcula_melhor_balda(cartas) #maior carta do naipe menos frequente

        return melhor_puxada

    def calcula_cartas_que_ainda_nao_sairam(self,cartas,cartas_que_ja_sairam,vaza=None):
        cartas_que_ainda_nao_sairam=copy.deepcopy(baralho_agente.cartas.saco)
        if cartas_que_ja_sairam.saco!=[]:
            [cartas_que_ainda_nao_sairam.remove(c) for c in cartas_que_ja_sairam.saco]
        if cartas.nb>0:
            [cartas_que_ainda_nao_sairam.remove(c) for c in cartas.saco]
        if vaza is not None:
            [cartas_que_ainda_nao_sairam.remove(c) for c in vaza.saco]

        cartas_que_ainda_nao_sairam_classe=cartas_class(cartas_que_ainda_nao_sairam)
        return cartas_que_ainda_nao_sairam_classe

    def calcula_prob_de_victoria_por_naipe(self,cartas,cartas_que_ainda_nao_sairam):
        
        casos_por_naipe_por_carta=[]
        for n in 'PEOC':
            casos=0
            minhas_cartas_por_naipe=0
            casos_por_naipe_por_carta_cumulativo=0
            for minha_carta in cartas.saco:
                if minha_carta['naipe']==n:
                    minhas_cartas_por_naipe+=1
                    for carta_possivel in cartas_que_ainda_nao_sairam.saco:
                        if carta_possivel['naipe']==n:
                            casos_por_naipe_por_carta_cumulativo+=1
                            if minha_carta['valor']>carta_possivel['valor']:
                                casos+=1
            
            if minhas_cartas_por_naipe>0 and casos_por_naipe_por_carta_cumulativo>0:
                casos_por_naipe_por_carta.append(casos/casos_por_naipe_por_carta_cumulativo*100)
            else:
                casos_por_naipe_por_carta.append(150) #para os casos onde o naipe está seco
        
        return casos_por_naipe_por_carta