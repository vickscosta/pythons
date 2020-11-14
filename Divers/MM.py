# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:09:55 2019

@author: costav
"""

#import random
#import collections
#from copy import deepcopy
import tkinter as tk


class MM:
    def __init__(self,parent):
        self.parent = parent
        self.canvas=tk.Canvas(parent)
        self.status=tk.Label(parent)
        self.drawboard()

            
    def drawboard(self,event=None):
        self.canvas.destroy()
        self.status.destroy()
        self.canvas=tk.Canvas(self.parent,width=500, height=500,bg="white")
        self.canvas.pack()
        self.bag={'r':self.canvas.create_oval(10,700,50,740,fill='red',outline='red'),
                  'o':self.canvas.create_oval(60,700,100,740,fill='orange',outline='orange'),
                  'y':self.canvas.create_oval(110,700,150,740,fill='yellow',outline='yellow'),
                  'g':self.canvas.create_oval(160,700,200,740,fill='green',outline='green'),
                  'b':self.canvas.create_oval(210,700,250,740,fill='blue',outline='blue'),
                  'p':self.canvas.create_oval(260,700,300,740,fill='purple',outline='purple')}
        self.ids={v:k for k,v in self.bag.items()}
        self.status=tk.Label(self.parent,text='                                         Costatech 2019                                    ',bg="white")
        self.canvas.create_line(0,680,400,680)
        self.canvas.create_line(0,60,400,60)
        self.canvas.create_line(0,760,400,760)
        self.canvas.create_line(200,760,200,820)
        self.canvas.create_text(150, 40,text="Four", font=("Arial",30) )
        self.canvas.create_text(50, 780,text="Computer", font=("Arial",12) )
        self.canvas.create_text(130, 780,text="Human", font=("Arial",12) )
        
        self.status.pack()
                
        self.parent.bind('<Control-n>',self.drawboard)
        self.parent.bind('<Control-N>',self.drawboard)
  
        
root=tk.Tk()
#root.geometry("310x825")
game=MM(root)
root.mainloop()