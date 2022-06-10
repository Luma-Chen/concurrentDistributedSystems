import socket
import threading

HOST = input("Host: ")
PORTA = int(input("Porta: "))

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen()
print(f'Servidor está ligado e escutando em {HOST}:{PORTA}')
clients = []
usernames = []

def globalMessage(message):
    for client in clients:
        client.send(message)


def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('ascii')
            globalMessage(
                f'{usernames[clients.index(client)]}: {receiveMessageFromClient}'.encode('ascii'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} deixou o chat...')
            globalMessage(
                f'{clientLeavedUsername} nos deixou...'.encode('ascii'))
            usernames.remove(clientLeavedUsername)


def initialConnection():
    while True:
        try:
            client, address = servidor.accept()
            print(f"Nova conexão: {str(address)}")
            clients.append(client)
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            usernames.append(username)
            globalMessage(
                f'{username} acabou de entrar no chat!'.encode('ascii'))
            user_thread = threading.Thread(
                target=handleMessages, args=(client,))
            user_thread.start()
        except:
            pass

initialConnection()