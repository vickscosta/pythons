import random
# import copy

#lista_cartas=lista_copas+lista_paus+lista_ouros+lista_espadas

def get_value(carta):
    return carta['valor']


class cartas_class():

    def __init__(self,cartas):

        self.nb=len(cartas)
        self.copas=[c for c in cartas if c['naipe']=='C']
        self.copas.sort(key=get_value)
        self.espadas=[c for c in cartas if c['naipe']=='E']
        self.espadas.sort(key=get_value)
        self.ouros=[c for c in cartas if c['naipe']=='O']
        self.ouros.sort(key=get_value)
        self.paus=[c for c in cartas if c['naipe']=='P']
        self.paus.sort(key=get_value)
        self.nb_copas=len(self.copas)
        self.nb_espadas=len(self.espadas)
        self.nb_ouros=len(self.ouros)
        self.nb_paus=len(self.paus)
        self.saco=cartas

    def baralha(self):

        saco=[c for c in self.saco]
        random.shuffle(saco)

        self.saco=saco


    def distribui_13_cartas(self):
               
        return [self.saco.pop() for _ in range(13)]

    # def ordena_cartas(self):
        
    #     cartas_naipe.sort(key=get_value)
    #     cartas_ordenadas+=cartas_naipe
    
    # def mostra_cartas(self):
    #     return[i['carta'] for i in self]

