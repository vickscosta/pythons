import random

lista_copas=[('AC',14,'C'),('2C',2,'C'),('3C',3,'C'),('4C',4,'C'),('5C',5,'C'),('6C',6,'C'),('7C',7,'C'),('8C',8,'C'),('9C',9,'C'),('10C',10,'C'),('VC',11,'C'),('DC',12,'C'),('KC',13,'C')]
lista_paus=[('AP',14,'P'),('2P',2,'P'),('3P',3,'P'),('4P',4,'P'),('5P',5,'P'),('6P',6,'P'),('7P',7,'P'),('8P',8,'P'),('9P',9,'P'),('10P',10,'P'),('VP',11,'P'),('DP',12,'P'),('KP',13,'P')]
lista_espadas=[('AE',14,'E'),('2E',2,'E'),('3E',3,'E'),('4E',4,'E'),('5E',5,'E'),('6E',6,'E'),('7E',7,'E'),('8E',8,'E'),('9E',9,'E'),('10E',10,'E'),('VE',11,'E'),('DE',12,'E'),('KE',13,'E')]
lista_ouros=[('AO',14,'O'),('2O',2,'O'),('3O',3,'O'),('4O',4,'O'),('5O',5,'O'),('6O',6,'O'),('7O',7,'O'),('8O',8,'O'),('9O',9,'O'),('10O',10,'O'),('VO',11,'O'),('DO',12,'O'),('KO',13,'O')]

_copas=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_copas]
_paus=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_paus]
_espadas=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_espadas]
_ouros=[{'carta':c[0],'valor':c[1],'naipe':c[2]} for c in lista_ouros]
_baralho=_copas+_paus+_espadas+_ouros

def get_value(carta):
    return carta['valor']

class cartas_class():

    def __init__(self,cartas=None):
        if cartas is None:
            self.saco=[]
        else:
            self.saco=cartas
        self.actualiza_saco()
        return

    def baralha(self):
        saco=[c for c in self.saco]
        random.shuffle(saco)
        self.saco=saco
        return

    def distribui_13_cartas(self):      
        return [self.saco.pop() for _ in range(13)]

    def mostra_cartas(self):
        return [i['carta'] for i in self.saco]

    def junta_cartas(self,cartas,actualisar=True):
        if type(cartas)==dict:
            self.saco.append(cartas)
        elif type(cartas)==cartas_class:
            for c in cartas.saco:
                self.saco.append(c)
        if actualisar:
            self.actualiza_saco()
    
    def actualiza_saco(self):
        self.nb=len(self.saco)
        self.copas=[c for c in self.saco if c['naipe']=='C']
        self.copas.sort(key=get_value)
        self.espadas=[c for c in self.saco if c['naipe']=='E']
        self.espadas.sort(key=get_value)
        self.ouros=[c for c in self.saco if c['naipe']=='O']
        self.ouros.sort(key=get_value)
        self.paus=[c for c in self.saco if c['naipe']=='P']
        self.paus.sort(key=get_value)
        self.nb_copas=len(self.copas)
        self.nb_espadas=len(self.espadas)
        self.nb_ouros=len(self.ouros)
        self.nb_paus=len(self.paus)
        self.damas=[c for c in self.saco if c['valor']==12]
        self.nb_damas=len(self.damas)
        self.homens=[c for c in self.saco if (c['valor']==11 or c['valor']==13)]
        self.nb_homens=len(self.homens)
        self.king=[c for c in self.saco if c['carta']=='KC']
        self.nb_king=len(self.king)
        self.saco=self.paus+self.ouros+self.espadas+self.copas

baralho_0=cartas_class(_baralho)

class baralho_class():
    def __init__(self):
        self.cartas=baralho_0
        return

    def atribui_carta(self,carta_a_encontrar):
        for carta in self.cartas.saco:
            if carta['carta']==carta_a_encontrar:
                return carta