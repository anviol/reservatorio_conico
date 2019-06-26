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

#lock = threading.RLock()
lock = 0

message = "Thread sendo executada: "
i = 0
tam = 200
stop_thread = 1

Cv = 0.5
R0 = 10.0
R1 = 100.0
H = 200.0
Pi = 3.141493
alpha = (R1 - R0)/H
href = 200.0
h_atual = 10.0

h = [0]*tam
Qout = 0.00
Qin = 10.00

tempo = [0]*tam

for x in range(tam):
   tempo[x] = x

def process_thread():
   global Cv, R0, R1, H, Pi, alpha, tam, h, Qout, Qin, lock, h_atual
   print("process_thread iniciou!")
   beta = 0.00
   for j in range(tam):
      #with lock:
      #lock.acquire()
      while lock == 1:
         i = 0
      lock = 1
      #print(str(Qin) + " process_thread")
      if j == 0:
         Qout = Cv*((h[j])**(1/2))
         #print("Qout " + str(Qout))
         beta = Pi*((R0 + alpha * h[j])**2)
         #print("beta " + str(beta))
         h[j] = Qout/beta + 1/beta*Qin
         #print("h[j] " + str(h[j]) + "\n")
         h_atual = h[j]
      else:
         Qout = Cv*((h[j-1])**(1/2))
         #print("Qout " + str(Qout))
         beta = Pi*((R0 + alpha * h[j-1])**2)
         #print("beta " + str(beta))
         h[j] = Qout/beta + 1/beta*Qin
         #print("h[j] " + str(h[j]) + "\n")
         h_atual = h[j]
      #lock.release()
      lock = 0
      time.sleep(0.2)

def softPLC_thread():
   global lock, Qin, tam, stop_thread, h_atual, href
   print("softPLC_thread iniciou!")
   #for k in range(tam):
   while stop_thread:
      #with lock:
      #lock.acquire()
      while lock == 1:
         i = 0
      lock = 1
      #print(str(Qin) + " softPLC_thread")
      if h_atual > href:
         Qin = Qin * (href / h_atual)
      if h_atual < href:
         Qin = Qin * (h_atual / href)
      else:
         Qin = Qin
      #lock.release()
      lock = 0
      time.sleep(0.2)

def synoptic_process():
   global stop_thread
   i = 0
   t1 = threading.Thread(target=process_thread)
   t2 = threading.Thread(target=softPLC_thread)
   t1.start()
   t2.start()
   while t1.isAlive():
      i = 0
   stop_thread = 0
   #while t2.isAlive():
      #i = 0


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