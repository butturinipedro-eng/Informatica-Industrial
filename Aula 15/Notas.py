"""
---API Socket---
  API socket CAI NA PROVA, fluxograma
  Começamos pelo servidor, criando um socket nele. Precisamos criar um objeto socket e para isso um classe socket
  Precisamos dizer qual classe de endereços o socket irá tratar (IPV4 etc) e dizer se vai ser um socket TCP (alta confibialidade e consumo alto de banda) UCP (baixa confiabilidade e baixo consumo de banda)
  Segundo passo: Bind (anexar) pede ao sistema operacional do servidor para fornecer um serviço em um IP e em uma porta, como se fosse um contrato de aluguel, estou dizendo "eu quero alugar a porta X para ealizar o serviço". 
  Só é possível ter um app por porta, se estiver outro aplicativo o bind da erro, gera uma excessão. Ip define a interface 
  Só com o bind o cliente não consegue se conectar.
  Para que o cliente consiga se conectar é preciso rodar o listen. O listen fala que o programa está pronto para receber conexões, "escute o serviço tal do IP tal e porta X"
  A partir do listen a conexão pode ser feita.
  Accept: Comando bloqueante -> bloqueia o fluxo da execução do programa, só continua após o cliente realizar a conexão. 
  Servidor não precisa saber o IP e a porta do cliente, mas o cliente precisa saber para passar essas informações para o connect.
  Feito isso é criado um tunel de comunicaão entre servidor e cliente. Agora a comunicação é tão simples quanto escrever em um arquvio
  Cliente escreve primeiro pois faz requerimentos ao servidor e o servidor responde e assim sucessivamente.
  No write escrevo bits, toda a comunicaão é feita por bits
  Protocolo é a forma como os bits são organizados.

----Modulo Socket----
  Métodos chamados bind, socket, write, listen etc. Métodos que invocam as primitivas do socket no sistema operacional

---Exceções---
  Problemas não previstos durante a construção do código
  Criar um mecanismo no programa para tratar essas excessões a fim de não quebrar o programa
    --Try e Accept--
    Ao inves do programa travar ele vai para o accept, assim evita o programa de travar, ou seja escolhemos a interrupção que vamos tratar e como tratá-la




"""
