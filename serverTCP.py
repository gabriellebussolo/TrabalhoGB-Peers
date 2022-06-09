import socket
import threading

# Coleta informacoes do IP do servidor atual
host = input('Insira o IP do servidor: ')
porta = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, porta))

print('Esperando peers se conectarem...')
s.listen(3)

newsocket1, endereco1 = s.accept()
print('connection from', endereco1)

newsocket2, endereco2 = s.accept()
print('connection from', endereco2)

newsocket3, endereco3= s.accept()
print('connection from', endereco3)

newsockets = ([newsocket1, newsocket2, newsocket3])
enderecos = [endereco1, endereco2, endereco3]
print('Conexões feitas, esperando por mensagens')

# Recebe mensagens do peer 1
def receive1(enderecos, *newsockets):
	while(True):
		comando = newsockets[0].recv(1024)
		id = -1
		if comando.decode().__contains__('*RETORNO* '):
			mensagem = comando.decode().split('|fonte|')
			for ip in enderecos:
				if mensagem[0].__contains__(ip[0]):
					id = enderecos.index(ip)
			recebeRetorno(mensagem[1], newsockets[id])

		else:
			recebeComando(comando, newsockets[0], newsockets)

# Recebe mensagens do peer 2
def receive2(enderecos, *newsockets):
	while(True):
		comando = newsockets[1].recv(1024)
		id = -1
		if comando.decode().__contains__('*RETORNO* '):
			mensagem = comando.decode().split('|fonte|')
			for ip in enderecos:
				if mensagem[0].__contains__(ip[0]):
					id = enderecos.index(ip)
			recebeRetorno(mensagem[1], newsockets[id])
		else:
			recebeComando(comando, newsockets[1], newsockets)

# Recebe mensagens do peer 3
def receive3(enderecos, *newsockets):
	while(True):
		comando = newsockets[2].recv(1024)
		id = -1
		if comando.decode().__contains__('*RETORNO* '):
			comando = comando.decode().split('|fonte|')
			for ip in enderecos:
				if comando[0].__contains__(ip[0]):
					id = enderecos.index(ip)
			recebeRetorno(comando[1], newsockets[id])

		else:
			recebeComando(comando, newsockets[2], newsockets)

# Metodo chamado quando a mensagem recebida eh um comando.
# Responsável por enviar para compartilhar o comando com os outros peers
def recebeComando(comando, newSocket, sockets):
	i = 0
	comando = comando.decode()
	comando =  '{}|fonte|{}'.format(newSocket.getpeername()[0], comando)
	while i < len(sockets):
		if sockets[i] != newSocket:
			sockets[i].send(comando.encode())
		i+=1

# Metodo chamado quando a mensagem recebida eh um retorno.
# Responsável por enviar o retorno dos peers para o peer que enviou o comando originalmente
def recebeRetorno(retorno, newSocket):
	newSocket.send(retorno.encode())

# Utilizacao de threads, pois o recv eh bloqueante
tRecebe1 = threading.Thread(target=receive1, args=(enderecos, newsockets[0], newsockets[1], newsockets[2]))
tRecebe2 = threading.Thread(target=receive2, args=(enderecos, newsockets[0], newsockets[1], newsockets[2]))
tRecebe3 = threading.Thread(target=receive3, args=(enderecos, newsockets[0], newsockets[1], newsockets[2]))

tRecebe1.start()
tRecebe2.start()
tRecebe3.start()
