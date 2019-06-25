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

message = "Thread sendo executada: "
i = 0

def process_thread():
   global message
   print(message + "process_thread" + ".")

def softPLC_thread():
   global message
   print (message + "softPLC_thread" + ".")

def synoptic_process():
   global message
   global i
   t1 = threading.Thread(target=process_thread)
   t1.start()
   t2 = threading.Thread(target=softPLC_thread)
   t2.start()
   print (message + "synoptic_process" + ".")

t = threading.Thread(target=synoptic_process)
t.start()

while t.isAlive():
   i = 0

print ("Threads morreram")
print ("Finalizando programa")

################################ Fim do Programa ###############################
