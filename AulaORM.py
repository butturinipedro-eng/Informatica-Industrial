"""
-----ORM-----
  Mapeamento objeto relacional / Object Relational Mapping
  Registros no banco de dados estar relacionado a objetos na memória
  Através da ORM é possível criar programas muito flexíveis, estruturação de código de forma genérica
  Registro é toda a linha de uma tabela
  Classe modela a tabela e os objetos são os registros
  Fazer trabalho utilizando ORM
  SGBD - Sistema de gerenciamento de banco de dados
  Cada App tem seu database: fácil manutenção
    Server SGBD
      |__DB1
      |   |__App1
      |       .
      |       .
      |       .
      |__DBn
          |__Appn

-----SQLAlchemy-----
  Core: camada de abstração entre programa e banco de dados
  1 - criar o engine (geralmente só uma engine por código)
  2 - Criar uma session de troca de informações (envio/requisições) posso ter várias sessões
  3 - 
