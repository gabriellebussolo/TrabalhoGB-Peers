import socket

# Coleta informacoes do IP do servidor atual
host = input('Insira o IP do servidor: ')
porta = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, porta))

print('Esperando peers se conectarem...')

# Cria uma lista de peers. Cada vez que o servidor receber que um peer quer se conectar, adiciona ele a essa lista
peers = []

while True:
    mensagem, endereco = s.recvfrom(128)
    print('IP do peer conectado: {}'.format(endereco))
    peers.append(endereco)
	
    if len(peers) == 3:        	
        # Pega as informacoes de cada peer da lista 'peers'          
        endereco1, porta1 = peers[0]
        endereco2, porta2 = peers[1]
        endereco3, porta3 = peers[2]
    
        # Compartilha os endereços (portas e IP) entre os peers conectados
        s.sendto('{} {}'.format(endereco2, endereco3).encode(), peers[0])  
        s.sendto('{} {}'.format(endereco1, endereco3).encode(), peers[1])
        s.sendto('{} {}'.format(endereco1, endereco2).encode(), peers[2])
