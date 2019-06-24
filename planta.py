import math as m
import numpy as np
import threading
import time
import socket
import struct

from tqdm import tqdm

class tanque (object):

    def __init__ (self,msg = ''):

        self.nivel = 5
        self.r1 = 5
        self.r0 = 1
        self.Cv = 1
        self.alfa = (self.r1 - self.r1)/(self.nivel)

        '''medidores de entrada e saida'''
        self.qin = 0
        self.qout = self.Cv*m.sqrt(self.nivel)


    '''funcao da classe {tanque} responsavel por simular,a cada '''
    '''instante de tempo, qual deve ser o proximo valor do tanque.nivel'''
    def atualizaNivel(self, periodo, msg):
        print(msg)
        novoNivel = 0
        if self.nivel >= 0:
            try:
                novoNivel = (((-self.Cv)*m.sqrt(self.nivel) + 1.0)*m.pow(m.pi*m.pow(self.r0+self.alfa*self.nivel,2),-0.5))*self.qin
                self.nivel = novoNivel
            except ValueError:

                print('tanque vazio')
                self.nivel = 0

        else:
            print('completamente vazio')
            self.nivel = 0

        time.sleep(periodo)
    #pass

'''cria variáveis principais do processo'''

dados = 0x00
t= tanque()
thr = threading.Thread(target=t.atualizaNivel, args=(1, "thread atulizaNivel: ON"))
thr.start()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#(IPV4,TCP-CONNECTION ORIENTED)
    print('socket criado com sucesso')
except:
    print('falha na criacao do socket, erro: %s'%err)

''' porta padrão de acesso ao socket'''
porta = 80


'''Instanciando Socket de comunicacao da planta'''
s.bind(('127.0.0.1', 80))
print('socket linkadão com a porta: %s'%(porta))

s.listen(5)
print('socket ouvindo ')

#dados = s.recv(1024)
#acaoControle = struct.unpack('!d',dados) #bytes -> float

while True:
    #Estabalece conexao com client
    try:
        '''Espera requisição da sala de controle'''
        cliente, addr = s.accept()
        print('conexao ao ip',addr)

        '''Envia agradecimento a sala de controle'''
        mensagem = 'Nivel: ' + str(t.nivel) + ' ----- Obrigado por conectar'
        cliente.send(mensagem.encode())
        
        '''recebe dados de controle'''
        dados = s.recv(1024)
        dadosDecod = struct.unpack('!d',dados) #bytes -> float
        print('comando de acao de controle (altura):', dadosDecod)

        '''Fecha conexão com cliente'''
        cliente.close()
    except:
        print('Esperando por conexoes')


    t.atualizaNivel(1,'atualiza nivel total')
