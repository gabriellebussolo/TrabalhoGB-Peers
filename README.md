## Trabalho Prático - Peers
 
O Trabalho Prático - Peers, consiste no segundo trabalho da disciplina de Redes de Computadores I. Nele, foi criado um software de terminal distribuído com três peers.
Cada peer possui função de servidor e de cliente. Além disso, há um servidor centralizado, no qual será utilizado para ter um controle dos peers conectados e para fazer o compartilhamento de mensagens entre eles.

Há três versões desse software, as quais utilizam protocolos diferentes. Os protocolos utilizados são: UDP, TCP e SCTP.

<p align="center">
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#serviços-usados">Serviços usados</a> • 
 <a href="#pré-requisitos">Pré-requisitos</a> • 
 <a href="#executando-o-projeto">Executando o projeto</a> • 
 <a href="#features">Features</a> • 
 <a href="#autora">Autora</a>
</p>
 
## Tecnologias 
  
* Python version 3.10.4
 
## Serviços usados
 
* Github
* Oracle VM Virtual Box version 6.1.26
* Wireshark version 3.6.5
 
## Pré-requisitos

Para executar os códigos SCTP, é necessário instalar a biblioteca libsctp-dev. Para isso, execute o seguinte código:
>    $ apt-get install libsctp-dev
 
## Executando o projeto

### Para executar o projeto SCTP, é necessário seguir os seguintes passos:
* Em um terminal, execute o código 'serverSCTP.py':
>    $ python3 serverSCTP.py

* Em outros três terminais, execute o código 'clientSCTP.py':
>    $ python3 clientSCTP.py

### Para executar o projeto TCP, siga os seguintes passos:
* Em um terminal, execute o código 'serverTCP.py':
>    $ python3 serverTCP.py

* Em outros três terminais, execute o código 'clientTCP.py':
>    $ python3 clientTCP.py

### Para executar o projeto UDP, é necessário seguir os seguintes passos:
* Em um terminal, execute o código 'serverUDP.py':
>    $ python3 serverUDP.py

* Em outros três terminais, execute o código 'clientUDP.py':
>    $ python3 clientUDP.py
 
## Features
 
* Envio de um comando em um peer para os outros peers
* Execução dos comandos em cada peer
* Coleta e envio da resposta do comando para o peer de origem do comando
* Apresentação dos retornos do comando de cada peer, no peer de origem do comando
 
## Autora
 
* **Gabrielle Bussolo**: @gabriellebussolo (https://github.com/gabriellebussolo)
