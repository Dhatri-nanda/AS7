# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwPmYsXZpErNoz1b_ATHwtH4gJ71JwiM
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from random import choices
import subprocess
import shlex


size  =100000
count = 0
#Let X=0,1,2 denote red and X=3,4,5,6,7,8 denote black
X = [0,1,2,3,4,5,6,7,8]
for i in range(size):
  count_red = 0
  chosen = random.sample(X,5)
  for i in range(4):
    if (chosen[i]<=2):
      count_red+=1
  if (count_red==1) and (chosen[4]<=2):
    count+=1


#plotting
cases = ["x = 1"]
prob_T = [0.19]
prob_S = [count/size]

x = np.arange(len(cases))
plt.stem(x + 0.00, prob_T, markerfmt='o',use_line_collection=True, basefmt=None , linefmt='orange' ,label='Theoritical')
plt.stem(x + 0.25, prob_S, markerfmt='o', use_line_collection=True, basefmt=None  ,linefmt='b', label='Simulated')
plt.xlabel('Cases')
plt.ylabel('Probability')
plt.xticks(x + 0.25/2,[1])
plt.legend()
plt.grid()
plt.show()