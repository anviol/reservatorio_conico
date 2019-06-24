import socket
import sys
import struct

'''codificacao da acao de controle para envio na rede'''
setPoint = 5.0
dados = struct.pack('!d',setPoint) #float -> byte

'''define em qual porta voce gostaria de conectar'''
porta = 80

'''cria socket do cliente'''
s = socket.socket()
print ('socket cliente criado com sucesso')

'''conecta no servidor localizado no pc local'''
s.connect(('127.0.0.1',porta))
print('conexao estabelecida com o sevidor')

''''Envia acao de controle'''
s.send(dados)
print('dados enviados com sucesso')

'''recebe dados do servidor'''
msgServidor = s.recv(1024)
print(msgServidor)

'''encerra conexao'''
s.close()
