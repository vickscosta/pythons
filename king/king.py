from cartas_src import cartas_class
from cartas_src import baralho_class
from jogo_src import jogo_class
from agente_src import agente_class
from jogador_src import jogador_class

from tkinter import *

root = Tk()
root.title("Welcome to King 1.0 by Costatech")

def create_cards():
    """
    create a list of 52 cards
    suit: club=C, diamond=D, heart=H spade=S
    rank: ace=A, 10=T, jack=J, queen=Q, king=K, numbers=2..9
    ace of spade would be SA, 8 of heart would be H8 and so on ...
    """
    return [ suit + rank for suit in "CDHS" for rank in "A23456789TJQK" ]
 
def shuffle_cards(card_list):
    """random shuffle a list of cards"""
    # make a copy of the original list
    card_list1 = card_list[:]
    # random.shuffle(card_list1)
    return card_list1
 
def pick_5cards(card_list):
    """pick five cards from the shuffled list"""
    return card_list[:5]
 
def create_images():
    """create all card images as a card_name:image_object dictionary"""
    card_list = create_cards()
    image_dict = {}
    for card in card_list:
        # all images have filenames the match the card_list names + extension .gif
        image_dict[card] = PhotoImage(file=image_dir+card+".gif")
        #print image_dir+card+".gif"  # test
    return image_dict
 
#def show_hand(event):
def show_hand(event):
    """create the card list, shuffle, pick five cards and display them"""
    root.title(card_list)  # test
 
    # now display the card images at the proper location on the canvas
    if idx==0 :
        x = 10
        y = 350
    elif idx==1 :
        x = 350
        y = 10
    elif idx==2:
        x = 350
        y = 350
    elif idx==3:
        x = 350
        y = 600
   
    for card in card_list:
        #print card, x, y  # test
        canvas1.create_image(x, y, image=image_dict[card], anchor=NW)
        # calculate each NW corner x, y
        x += 30 #90
 
# change this to the directory your card GIFs are in
image_dir = "C:/Users/vicks/Documents/Python Scripts/pythons/king/cards/"
 
# load a sample card to get the size
photo1 = PhotoImage(file=image_dir+"C2.gif")
 
# make canvas 13 times the width of a card + 100
width1 = 13 * photo1.width() + 100
height1 = photo1.height() + 20
canvas1 = Canvas(bg='green',width=1200, height=800)
#canvas1 = Canvas(bg='green',width=width1, height=height1)
canvas1.pack()
 
# now load all card images into a dictionary
image_dict = create_images()
#print image_dict  # test
 
VER_CARTAS_AO_INICIO=False

baralho=baralho_class()

# jogador=[jogador_class(idx) for idx in range(4)]
jogador=[None for _ in range(4)]
jogador[0]=jogador_class(0,'Especialista')
jogador[1]=jogador_class(0,'Normal')
jogador[2]=jogador_class(0,'Medricas')
jogador[3]=jogador_class(0,'Humano')

# 'Humano', 'Medricas', 'Normal', 'Burro', 'Especialista'

def mostra_cartas_dos_jogadores(jogadores):

    for j in jogadores:
        print('P', j.idx,':',j.mao.mostra_cartas())
    return

score_list=[]
NB_JOGOS=1

for nb_jogos_king in range(NB_JOGOS):
    king=jogo_class()
    for j in jogador:
        j.pontos=0
    print('\n*********************************')
    print('*******  JOGO',nb_jogos_king,'*****************')
    print('*********************************')
    
    for game in range(2):

        king.prepara_partida(baralho.cartas,jogador)

        if VER_CARTAS_AO_INICIO:
            mostra_cartas_dos_jogadores(jogador) 

        for j in jogador:
            old_card_list=j.mao.mostra_cartas()

            card_list=[]
            for c in old_card_list:
                if len(c)==3:
                    c1='T'
                    c2=c[2]
                else:
                    c1=c[0]
                    c2=c[1]

                c1=c1.replace("V","J")
                c1=c1.replace("D","Q")
                
                c2=c2.replace("C","H")
                c2=c2.replace("E","S")
                c2=c2.replace("O","D")
                c2=c2.replace("P","C")
                card_list.append(c2+c1)
            
            idx=j.idx

            # bind left mouse click on canvas to next_hand display
            canvas1.bind('<Button-1>', show_hand)
        
        root.mainloop()


        king.começa_partida(jogador)

        print('\n')
        print(king.nome_partida, [j.pontos_partida for j in jogador])
        print('Total',[j.pontos for j in jogador])
    
    score_list.append([j.pontos for j in jogador])

# print('\n',score_list)    

avg_score=[0,0,0,0]
sum_score=[0,0,0,0]
for score in score_list:
    for idx,j in enumerate(score):
        sum_score[idx]+=j

for i in range(4):
    avg_score[i]=sum_score[i]/len(score_list)

#print('\n',score_list)   
print('\n',avg_score)
    


