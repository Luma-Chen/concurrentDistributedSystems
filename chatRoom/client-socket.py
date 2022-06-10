import socket
import threading

ServerIP = input("Servidor IP: ")
PORT = int(input("Porta: "))

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    nomeUsuario= input('Digite seu nome: ')
    cliente.connect ((ServerIP,PORT))
    print(f'Conectado com sucesso ao {ServerIP}:{PORT}')
except:
    print(f'ERRO: Por favor, verifique sua entrada: {ServerIP}:{PORT}')

def receiveMessage():
    while True:
        try:
            message = cliente.recv(2048).decode('ascii')
            if message=='getUser':
                cliente.send(nomeUsuario.encode('ascii'))
            else:
                print(message)
        except:
            print('ERRO: Cheque sua conexão ou seu servidor pode estar offline')

def sendMessage():
    while True:
        cliente.send(input().encode('ascii'))

thread1 = threading.Thread(target=receiveMessage,args=()) 
thread2 = threading.Thread(target=sendMessage,args=())
thread1.start()
thread2.start()