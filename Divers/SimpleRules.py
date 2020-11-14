import random

NB_GENES=100
NB_LIGNES=100

connections=[[random.randint(1,NB_GENES),random.randint(1,NB_GENES),random.randint(1,NB_GENES)] for x in range(NB_GENES)]

def go_random():
    return random.choice(['X','_'])

def make_crossings(liste,connections,decoder):
    new=[]
    for c in connections:
        value=''
        for t in c:
            value+=liste[t-1]

        for d in decoder:
            if d[0]==value:
                new.append(d[1])
    return new

decoder=[('___',go_random()),
         ('__X',go_random()),
         ('_X_',go_random()),
         ('_XX',go_random()),
         ('X_X',go_random()),
         ('X__',go_random()),
         ('XX_',go_random()),
         ('XXX',go_random())]

generation0=[go_random() for x in range(NB_GENES)]
[print(x,end='') for x in generation0]

old_generation=generation0
for i in range(NB_LIGNES): 
    new_generation=make_crossings(old_generation,connections,decoder)
    print('')
    [print(x,end='') for x in new_generation]
    old_generation=new_generation

# print('\n',decoder)