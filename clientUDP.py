import socket
import threading
import subprocess

# Coleta informacoes de endereço IP do peer atual e do servidor de destino
host = input('Insira o endereço IP de origem: ')
porta = 6001
servidor = input('Insira o endereço IP do servidor: ')
portaservidor = 6000

# Cria o socket e envia para o servidor uma notificacao para tentar a conexao
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, porta))
s.sendto('peer conectando-se'.encode(), (servidor, portaservidor))

# Recebe as informacoes dos dois outros peers conectados
peers = s.recv(1024).decode()
ip1, ip2 = peers.split(' ')

print('\nPeers conectados:')
print('# IP peer 1: %s' % (ip1))
print('# IP peer 2: %s' % (ip2))
print()

# Recebe mensagens dos outros peers
def receber():
    while True:
        mensagem, enderecoPeerFonte = s.recvfrom(1024)

        if mensagem.decode().__contains__('*RETORNO* '):
            retorno2, enderecoPeerFonte2 = s.recvfrom(1024)
            print('Peer {}\n'.format(enderecoPeerFonte))
            mensagem = mensagem.decode().replace('*RETORNO* ', '')
            print(mensagem)
            print('-------------------------------------------------------------------')

            print('Peer {}\n'.format(enderecoPeerFonte2))
            retorno2 = retorno2.decode().replace('*RETORNO* ', '')
            print(retorno2)
            print('-------------------------------------------------------------------')

        else:
            print('Peer %s | comando %s\n' % (host, mensagem.decode()))
            comando = mensagem.decode().split(' ')
            try:
                subprocess.run(comando)
            except Exception as e:
                print(e)

            try:
                retorno = subprocess.run(comando, capture_output=True, text=True)
                certo = '*RETORNO* ' + retorno.stdout
                s.sendto(certo.encode(), enderecoPeerFonte)
            except Exception as e:
                erro = '*RETORNO* ' + str(e)
                s.sendto(erro.encode(), enderecoPeerFonte)

            print('-------------------------------------------------------------------')

#Thread utilizada, pois o recv é bloqueante
tRecebe = threading.Thread(target=receber)
tRecebe.start()

# Envia mensagens para os peers
while True:
    comando = input()

    print('Peer %s | comando %s\n' % (host, comando))
    comandolist = comando.split(' ')
    try:
        subprocess.run(comandolist)
    except Exception as e:
        print(e)
    print('-------------------------------------------------------------------')

    s.sendto(comando.encode(), (ip1, porta))
    s.sendto(comando.encode(), (ip2, porta))
