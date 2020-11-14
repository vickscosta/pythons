
import tkinter as tk

root=tk.Tk()
#root.geometry("310x825")

class MM:
    def __init__(self,parent):
        self.parent = parent
        self.canvas=tk.Canvas(parent)
        self.status=tk.Label(parent)
        self.colors={'r':'red','o':'orange','y':'yellow','g':'green','b':'blue','p':'purple'}
        self.HumanGuesses=True
        self.drawboard()

            
    def drawboard(self,event=None):
        self.canvas.destroy()
        self.status.destroy()
        self.canvas=tk.Canvas(self.parent,width=310, height=815,bg="white")
        self.canvas.pack()
        self.bag={'r':self.canvas.create_oval(10,700,50,740,fill='red',outline='red'),
                  'o':self.canvas.create_oval(60,700,100,740,fill='orange',outline='orange'),
                  'y':self.canvas.create_oval(110,700,150,740,fill='yellow',outline='yellow'),
                  'g':self.canvas.create_oval(160,700,200,740,fill='green',outline='green'),
                  'b':self.canvas.create_oval(210,700,250,740,fill='blue',outline='blue'),
                  'p':self.canvas.create_oval(260,700,300,740,fill='purple',outline='purple')}
        self.ids={v:k for k,v in self.bag.items()}
        self.guesses=['']
        self.status=tk.Label(self.parent,text='                                         Costatech 2019                                    ',bg="white")
        self.canvas.create_line(0,680,400,680)
        self.canvas.create_line(0,60,400,60)
        self.canvas.create_line(0,760,400,760)
        self.canvas.create_line(200,760,200,820)
        self.canvas.create_text(150, 40,text="MASTERMIND", font=("Arial",30) )
        self.canvas.create_text(50, 780,text="Computer", font=("Arial",12) )
        self.canvas.create_text(130, 780,text="Human", font=("Arial",12) )
        
        if self.HumanGuesses==True:
            computerRcolor='white'
            humanRcolor='red'
            inputR1color='white'
            inputR2color='white'
            inputR3color='light grey'
            self.Code=[random.choice(MYCHOICES) for _ in range(NBCODE)]
            self.CodeColorCount=collections.Counter(self.Code)
            print(self.Code)
        else:
            computerRcolor='red'
            humanRcolor='white'
            inputR1color='black'
            inputR2color='yellow'
            inputR3color='red'
            [self.canvas.itemconfig(j,fill='light grey',outline='black') for j in self.ids]
            
        self.options={'computer':self.canvas.create_rectangle(45,800,60,815,fill=computerRcolor,outline='black'),
                      'human':self.canvas.create_rectangle(125,800,140,815,fill=humanRcolor,outline='black')}
        self.id_options={v:k for k,v in self.options.items()}
        
        #empty circles
        for i in range(NBCODE):
            for j in range(MAXGUESSES):
                self.canvas.create_oval(10+i*50,630-j*50,50+i*50,670-j*50,outline='black')
        
        #empty squares
        self.bag_squares={}
        for j in range(MAXGUESSES):
            self.bag_squares['R1-'+str(j)]=self.canvas.create_rectangle(230,640-50*j,255,650-50*j,outline='black')
            self.bag_squares['R2-'+str(j)]=self.canvas.create_rectangle(260,640-50*j,285,650-50*j,outline='black')
            self.bag_squares['R3-'+str(j)]=self.canvas.create_rectangle(230,655-50*j,255,665-50*j,outline='black')
            self.bag_squares['R4-'+str(j)]=self.canvas.create_rectangle(260,655-50*j,285,665-50*j,outline='black')
        
        #input squares
        self.bag_inputs={'black':self.canvas.create_rectangle(230,770,255,785,fill=inputR1color,outline='black'),
                         'yellow':self.canvas.create_rectangle(230,795,255,810,fill=inputR2color,outline='black'),
                         'go':self.canvas.create_text(280,790,text="GO", font=("Arial",10),fill=inputR3color)}
        self.id_input={v:k for k,v in self.bag_inputs.items()}
        
        self.status.pack()
                
        self.canvas.bind('<1>',self.clique)
        self.parent.bind('<Control-n>',self.drawboard)
        self.parent.bind('<Control-N>',self.drawboard)
 
     
    def clique(self,event=None):
        if len(self.canvas.find_withtag("current"))==0:
            return
        
        elif self.canvas.find_withtag("current")[0] in self.id_options:
            self.changeplaymode()
            
        elif self.canvas.find_withtag("current")[0] in self.ids and self.HumanGuesses==True:
            id=self.canvas.find_withtag("current")[0]
            self.youplay(id)
            
        elif self.canvas.find_withtag("current")[0] in self.id_input and self.HumanGuesses==False:
            id=self.canvas.find_withtag("current")[0]
            self.human_action(id)
        
        else:
            return            

    
    def changeplaymode(self,event=None):
        if self.HumanGuesses==True:
            self.HumanGuesses=False
            self.drawboard()
            self.init_iplay()
        elif self.HumanGuesses==False:
            self.HumanGuesses=True
            self.drawboard()
        
    
    def init_iplay(self,event=None):

        self.listepossible=self.initarbre()
        self.scorelist=[]
        self.keylist=[]
    
        #first guess
        for _ in range(NBCODE):
            guess=random.choice(MYCHOICES)
            self.guesses[-1]+=guess
            self.print_ball(guess)


    def human_action(self,aid,event=None):
        self.get_key_coordinates()
        countkeys=len(self.scorelist)
        
        if aid==self.bag_inputs['black'] and countkeys<NBCODE:
            self.scorelist.append(self.id_input[aid])
            self.canvas.create_rectangle(self.key_coordinates[countkeys],fill='black',outline='black')
            
        elif aid==self.bag_inputs['yellow'] and countkeys<NBCODE:
            self.scorelist.append(self.id_input[aid])
            self.canvas.create_rectangle(self.key_coordinates[countkeys],fill='yellow',outline='black')
            
        elif aid==self.bag_inputs['go']:
            self.keylist.append((collections.Counter(self.scorelist)['black'],collections.Counter(self.scorelist)['yellow']))
            self.scorelist=[]
            
            if self.keylist[-1][0]==4:
                self.status.config(text='I win in {} guesses. Press Ctrl-N pour recommencer.'.format(len(self.guesses)))
                self.canvas.unbind('<1>')
            else:
                newlist=[]
                for idx,i in enumerate(self.listepossible):
                    if self.score_fonction(self.guesses[-1],i)==self.keylist[-1]:
                        newlist.append(i)
                if len(newlist)==0:
                    self.status.config(text='YOU LIED! Press Ctrl-N pour recommencer.')
                    self.canvas.unbind('<1>')
                    return
                self.guesses.append(random.choice(newlist))
                self.listepossible = deepcopy(newlist)
                self.print_ball(self.guesses[-1],allatonce=True)

    
    def initarbre(self,event=None):
        alistepossible=[]
        for i1 in MYCHOICES:
            for i2 in MYCHOICES:
                for i3 in MYCHOICES:
                    for i4 in MYCHOICES:
                        alistepossible.append(i1+i2+i3+i4)
        return alistepossible
 
    
    def youplay(self,aid,event=None):
        guess=self.ids[aid]
        self.guesses[-1]+=guess
        self.print_ball(guess)
        if len(self.guesses[-1])<4:
            return
        
        (noir,blanc)=self.score_fonction(self.Code,self.guesses[-1])
        colors=noir*['black']+blanc*['yellow']
        self.get_key_coordinates()
        for color,coord in zip(colors,self.key_coordinates):
            self.canvas.create_rectangle(coord,fill=color,outline='black')
        
        if noir==4:
            self.status.config(text='You win in {} guesses.'.format(len(self.guesses)))
            self.canvas.unbind('<1>')
        elif len(self.guesses) > MAXGUESSES-1:
            self.status.config(text='Game over! The correct answer is {}.'.format(''.join(self.Code)))
            self.canvas.unbind('<1>')
        else:
            self.guesses.append('')

            
    def score_fonction(self,acode1,acode2,event=None):
        ColorCount1=collections.Counter(acode1)
        ColorCount2=collections.Counter(acode2)
        lblanc=sum(min(ColorCount1[k],ColorCount2[k]) for k in ColorCount1)
        lnoir=sum(a==b for a,b in zip(acode1,acode2))
        lblanc-=lnoir
        return lnoir,lblanc
        
    
    def print_ball(self,aguess,allatonce=False,event=None):
        if not(allatonce):
            self.get_offset_coordinates()
            self.canvas.create_oval(self.x_offset,self.y_offset,
                                    self.x_offset+40,self.y_offset+40,
                                    fill=self.colors[aguess],outline='black')
        else:
            for i in range(NBCODE):
                self.get_offset_coordinates(i)
                self.canvas.create_oval(self.x_offset,self.y_offset,
                                    self.x_offset+40,self.y_offset+40,
                                    fill=self.colors[aguess[i]],outline='black')
     
    
    def get_offset_coordinates(self,aiteration=-1,event=None):
        self.y_offset=630-(len(self.guesses)-1)*50
        if aiteration!=-1:
            self.x_offset=10+(aiteration)*50
        else:
            self.x_offset=10+(len(self.guesses[-1])-1)*50
    
    def get_key_coordinates(self,event=None):
        self.key_coordinates=[(230,self.y_offset+10,255, self.y_offset+20),
                             (260,self.y_offset+10,285, self.y_offset+20),
                             (230,self.y_offset+25,255, self.y_offset+35),
                             (260,self.y_offset+25,285, self.y_offset+35)]

game=MM(root)
root.mainloop()