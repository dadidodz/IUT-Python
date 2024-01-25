# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:06:06 2020

@author: Dorian
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle


f = open('data1(1).txt', 'rb')
x = pickle.load(f, encoding='iso8859')
f.close
print(x)

print(sum(x)[0]/np.shape(x)[0])
print(sum(x)[0])

