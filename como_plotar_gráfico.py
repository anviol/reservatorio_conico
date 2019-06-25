import matplotlib.pyplot as plt
import numpy as np
import random as rand
import simple_pid as pid

Cv = 0.5
R0 = 100
R1 = 10
H = 10
Pi = 3.14
alpha = (R1 - R0)/H

tam = input('Digite o range do array: ')

try:
   tam = int(tam)
except ValueError:
   print("O valor digitado não é um número")
   exit()

h = [0]*tam
Qout = [0]*tam
Qin = [0]*tam

for i in range(tam):
   h[i] = i
   Qout [i] = Cv * (h[i]**0.5)



plt.plot( h, Qout)
plt.title("Volume X Altura")
plt.show()
