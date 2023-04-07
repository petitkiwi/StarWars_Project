import random
from math import pi, sin
import matplotlib.pyplot as plt
import time

f = open('position_sample.csv','r')
f.readline() # sauter 1re ligne (#t;x;y)

sample_list=[]
for line in f: # transformer chaque ligne en liste de 3 valeurs t, x et y
    sample_list.append(line.strip().split(';')) # strip() pour suppr l'espace en fin de ligne

for i in range(len(sample_list)): # convertir string en float
    for j in range(3):
        sample_list[i][j]=float(sample_list[i][j])
       

class individu:
    def __init__(self,p1=None,p2=None,p3=None,p4=None,p5=None,p6=None):
        if(p1==None):
            self.p1=random.uniform(13.15,13.25)
            self.p2=random.uniform(-21.15,-21.1)
            self.p3=random.uniform(26.2,26.3)         
            self.p4=random.uniform(-22.9,-22.8)
            self.p5=random.uniform(41,41.15)
            self.p6=random.uniform(-94.45,-94.3)
        else:
            self.p1=p1
            self.p2=p2
            self.p3=p3
            self.p4=p4
            self.p5=p5
            self.p6=p6
                      
        self.coeff_erreur=self.fitness()
            
    def __str__(self):
        return (f"p1 ={self.p1}"+
                f" p2 ={self.p2}"+
                f" p3 ={self.p3}"+'\n'+
                f"p4 ={self.p4}"+
                f" p5 ={self.p5}"+
                f" p6 ={self.p6}"+'\n'+
                f"Coût ={self.coeff_erreur}") 
                # formattage pour ne garder que 3 chiffres après la virgule
            
    def fitness(self): # carré de la différence entre valeur estimée et valeur empirique
        coeff_erreur_x=0
        coeff_erreur_y=0
        for i in range(len(sample_list)):
            coeff_erreur_x+=(xy(sample_list[i][0],self.p1,self.p2,self.p3) - sample_list[i][1])**2
            coeff_erreur_y+=(xy(sample_list[i][0],self.p4,self.p5,self.p6) - sample_list[i][2])**2
        self.coeff_erreur = coeff_erreur_x + coeff_erreur_y   
        return self.coeff_erreur


def xy(t,pA,pB,pC):
    return pA*sin(pB*t+pC)
        
def evaluate(pop):
    return sorted(pop,key=lambda ind: ind.coeff_erreur)
        
def create_rand_pop(count):
    l = []
    for i in range(count):
        l.append(individu())
    return l
        
def selection(pop,best,worst):
    pop2=list()
    for i in range(best):
        pop2.append(pop[i])            
    for i in range(worst):
        pop2.append(pop[len(pop)-i-1])
    return pop2

def croisement(ind1,ind2): # croisement alternance 1 sur 2
    return [individu(p1=ind1.p1,p2=ind2.p2,p3=ind1.p3,p4=ind2.p4,p5=ind1.p5,p6=ind2.p6),
            individu(p1=ind2.p1,p2=ind1.p2,p3=ind2.p3,p4=ind1.p4,p5=ind2.p5,p6=ind1.p6)]
    
def mutation(ind): 
    randIndex=random.randint(1,6)
    if(randIndex==1):
        ind.p1=random.uniform(13.15,13.25) 
    elif(randIndex==2):
        ind.p2=random.uniform(-21.2,-21)
    elif(randIndex==3):
        ind.p3=random.uniform(26.2,26.3)
    elif(randIndex==4):
        ind.p4=random.uniform(-23,-22.8)
    elif(randIndex==5):
        ind.p5=random.uniform(41,41.15)
    elif(randIndex==6):
        ind.p6=random.uniform(-94.45,-94.3)  
    return ind
    
    
def algoG():
    pop=create_rand_pop(30) # création d'une population
    solution=False
    nb_iteration=0
    
    while not solution:
        evaluation=evaluate(pop)
        if(evaluation[0].fitness()<2):
            solution=True
        else:
            select=selection(evaluation,10,4) # les 10 meilleurs + les 4 pires
            croises=[]
            for i in range(0,len(select),2):
                croises+=(croisement(select[i],select[i+1]))
            mutes=[]
            mutes.append(mutation(pop[random.randint(0,len(pop)-1)]))
            newrand=create_rand_pop(10)
            pop=select[:]+croises[:]+mutes[:]+newrand[:]
            
        nb_iteration+=1
        print("\nItération numéro :",nb_iteration)
        print(evaluation[0])
    
    print(f"Temps d'exécution : {((time.time() - start_time)*1000)} ms") # temps d'execution
    
    for i in range(len(sample_list)): # création graphe
        plt.plot(sample_list[i][1],sample_list[i][2],'ro',color='cornflowerblue',markersize=6)
        plt.plot(xy(sample_list[i][0],evaluation[0].p1,evaluation[0].p2,evaluation[0].p3),
             xy(sample_list[i][0],evaluation[0].p4,evaluation[0].p5,evaluation[0].p6),'r+',color='red')
        
    plt.axis([-15, 15, -25, 25])
    plt.xlabel('x(t) = p1 × sin(p2 × t + p3)')
    plt.ylabel('y(t) = p4 × sin(p5 × t + p6)')
    plt.title('Precision of the solution')
    plt.show()
        

start_time = time.time() # lancement du timer
algoG()
  
