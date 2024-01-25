# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:27:25 2020

@author: Dorian
"""

import matplotlib.pyplot as plt
import numpy as np

#exemple 4
x = [56, 68, 35, 41]
a = []
for i in range (len(x)):
    for j in range (x[]):
        x.append()
plt.hist(x)
plt.show()

#exemple 5
fig = plt.figure()
x = [1, 2, 3, 4, 5]
height = [442, 75, 49, 12, 20]
width = 0.5
plt.bar(x, height, width, color='b' )
plt.show()

#exemple 7
fig = plt.figure()
names = ['Vert', 'Bleu', 'Jaune']
height = [15, 12, 28]
width = 0.5
plt.bar(names, height, width, color='b' )
plt.show()

#exemple 8
labels = 'Gauche', 'Extreme', 'Autres', 'Droite', 'Centre'
sizes = [13.8, 24.1, 8.0, 19.5, 34.5]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Résultats du premier tour")
plt.show()

