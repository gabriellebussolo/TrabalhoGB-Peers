import socket
import threading
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_SCTP)
host = input('Insira o IP do cliente: ')
porta = 9000
s.bind((host, porta))

server = input('Insira o IP do servidor: ')

s.connect((server, porta))
print('Conectado ao servidor ' + server)

# Recebe mensagens do servidor
def receber():
	while True:
		mensagem = s.recv(1024)

		if mensagem.decode().__contains__('*RETORNO* '):
			mensagem = mensagem.decode().replace('*RETORNO* ', '')
			mensagem = mensagem.split(' |ip')

			retorno2 = s.recv(1024)
			retorno2 = retorno2.decode().replace('*RETORNO* ', '')
			retorno2 = retorno2.split(' |ip')

			print('Peer {}\n'.format(mensagem[0]))
			print(mensagem[1])
			print('-------------------------------------------------------------------')

			print('Peer {}\n'.format(retorno2[0]))
			print(retorno2[1])
			print('-------------------------------------------------------------------')

		else:
			comando = mensagem.decode().split('|fonte|')
			print('Peer %s | comando %s\n' % (host, comando[1]))
			ipFonte = comando[0]
			comando = comando[1].split(' ')
			
			try:
				subprocess.run(comando)
			except Exception as e:
				print(e)

			try:
				retorno = subprocess.run(comando, capture_output=True, text=True)
				certo = ipFonte + '|fonte|' + '*RETORNO* ' + host + ' |ip' + retorno.stdout
				s.sendto(certo.encode(), (server, porta))
			except Exception as e:
				erro = ipFonte + '|fonte|' + '*RETORNO* ' + host + ' |ip' + str(e)
				s.sendto(erro.encode(), (server, porta))

			print('-------------------------------------------------------------------')

#Thread utilizada, pois o recv é bloqueante
tRecebe = threading.Thread(target=receber)
tRecebe.start()

# Envia mensagens para o servidor
while True:
	comando = input('> ')
	
	s.sendto(comando.encode(), (server, porta))

	print('Peer %s | comando %s\n' % (host, comando))
	comandolist = comando.split(' ')
	
	try:
		subprocess.run(comandolist)
	except Exception as e:
		print(e)
	print('-------------------------------------------------------------------')