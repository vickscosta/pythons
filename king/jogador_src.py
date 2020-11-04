from cartas_src import cartas_class

class jogador_class():

    def __init__(self,idx):
        self.idx=idx
        self.agente='Humano'
        self.pontos=0
    
    def apanha_mao(self,mao):
        self.mao=mao

        