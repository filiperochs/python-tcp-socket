import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Escreva sua mensagem:')
msg = input().encode()
while True:
    tcp.send(msg)
    msgRecv = tcp.recv(1024)
    print('Mensagem Recebida:')
    print(msgRecv.decode())
    tcp.close()
    exit()
    