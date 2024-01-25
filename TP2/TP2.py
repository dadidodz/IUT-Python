# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:11:52 2020

@author: Dorian
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

#Question 1
#Lecture du fichier de données
f = open('data2.txt', 'rb')
x = pickle.load(f, encoding='iso8859')
f.close

#Nombre de communes en France
nbCommunes = x.shape[0]
print("Il y a " + str(nbCommunes) + " communes en France.")

#Calcul de la moyenne
moyenne = sum(x)[0]/x.shape[0]
print("La moyenne d'habitants par commune est de : " + str(moyenne))

#Valeur minimale dans le fichier 
#Valeur du plus petit nombre d'habitants dans une commune
nbMinHab = min(x)[0]
nbMaxHab = max(x)[0]
print("La commune aillant le moins d'habitant est de " + str(nbMinHab) + 
          ".\nLa commune aillant le moins d'habitant est de " + str(nbMaxHab))
#plt.hist(x, density=True, log=True)
"""
#HISTOGRAMME
plt.hist(x, range = (0, 500), bins = 2, color = 'yellow',edgecolor = 'red')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')


#Calcul de l'écart-type

resultat = 0.0

for i in range(len(x)):
    resultat+=(x[i]-moyenne)**2
    print(resultat)
    
ecarttype=resultat/len(x)
print(ecarttype)


#Calcul de la médiane
a=int(len(x)/2)
b=int((len(x)/2)+1)
print(a)
print(b)
c=x[a]
print(c)
mediane =sorted(x)[int(len(x)/2)+len(x)%2]
print(mediane)
#print(x)[36662]
"""
mediane =sorted(x)[int(len(x)//2+len(x)%2)]
print(mediane)
#ecarttype= np.sqrt(x @ x / len(x) - moyenne * moyenne)
#t = arange(m -2 * s, m+2*s, s/50)
#g = exp(-(t-m)**2 / 2 / s**2)/2.5/s