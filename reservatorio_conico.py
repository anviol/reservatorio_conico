################################################################################
#                                                                              #
#                        Trabalho Pratico Final de ATR                         #
#                              Reservatorio Conico                             #
#                                                                              #
# Professor: Armando Alves Neto                                                #
#                                                                              #
# Nome: Andre Vinicius de Oliveira          Matricula: 2013065935              #
# Nome: Luiz Gabriel Aragão Oliveira        Matricula:2014086480               #
#                                                                              #
# Versão: 1.00                                                                 #
# Data: 22/05/2019                                                             #
#                                                                              #
#                                 Python 3.7.3                                 #
################################################################################
import threading
import time
import matplotlib.pyplot as plt
import random as rand

lock = threading.Lock()

message = "Thread sendo executada: "
i = 0

Cv = 0.5
R0 = 100
R1 = 10
H = 10
Pi = 3.14
alpha = (R1 - R0)/H

tam = 10

h = [0]*tam
Qout = 0.00
Qin = 2.00

tempo = [0]*tam

for x in range(tam):
   tempo[x] = x

def process_thread():
   global Cv, R0, R1, H, Pi, alpha, tam, h, Qout, Qin, lock
   beta = 0.00
   for j in range(tam):
      lock.acquire()
      print(str(Qin) + " process_thread")
      Qout = Cv*((h[j])**(1/2))
      beta = Pi*((R0 + alpha * h[j])**2)
      h[j] = Qout/beta + 1/beta*Qin
      lock.release()

def softPLC_thread():
   global lock, Qin, tam
   lock.acquire()
   for k in range(tam):
      print(str(Qin) + " softPLC_thread")
      Qin = Qin + 10.0
   lock.release()

def synoptic_process():
   i = 0
   t1 = threading.Thread(target=process_thread)
   t2 = threading.Thread(target=softPLC_thread)
   t1.start()
   t2.start()
   while t1.isAlive():
      i = 0
   while t2.isAlive():
      i = 0


t = threading.Thread(target=synoptic_process)
t.start()

while t.isAlive():
   i = 0

plt.plot(tempo, h)
plt.title("Volume X Altura")
plt.show()

print ("Threads morreram")
print ("Finalizando programa")

################################ Fim do Programa ###############################
