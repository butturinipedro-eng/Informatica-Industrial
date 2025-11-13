"""
----Software Supervisório-----
Monitorar e supervisionar dados da planta e operar a planta
Coleta de dados -> protocolos Ex: modbus
Supervisão da máquina -> IHM
Armazenamento de dados -> Banco de dados

----MODBUS----
Comunicação entre CLPs, processa e automatiza plantas industriais
TCP/IP - porta padrão 502, operação simplificada, via rede
Servidor modbus são os equipamentos de campo. Ex: medidores
O cliente é o software q se conecta ao servidor
Unit Id serve para conectar a algum dispostivo especifico de um modo serial
No servidor há uma tabela de dados na qual há vários endereços e dados relacionados
No function code podemos falar: quero escrever um dado de 16 bits na tabela de holding na posição 150 ou ler o dado da bobina na posição 1
Modbus foi criado para transmitir bits e numero inteiro mas é possível  fazer adptações para utilizar floats.
Basicamente o que fazemos como cliente é ler e escrever dados na tabela
Supervisório só le e envia dados, o CLP faz coisas a partir desse código
