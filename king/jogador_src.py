class jogador_class():

    def __init__(self,idx):
        self.idx=idx
        self.agente='Humano'
        self.pontos=0
        self.mao=[]
    
    def junta_carta(self,carta):
        self.mao+=carta

        