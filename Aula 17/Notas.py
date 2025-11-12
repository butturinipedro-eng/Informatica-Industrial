"""
Todo servidor tem no minimo 1 thread
para cada cliente que eu recebo eu adiciono um thread, além da thread principal. Ou seja, n+1, se 10 clientes se conectam eu tenho 11 threads.
processo tem stack, heap, registradores e memoria de programa
variaveis locais não são compartilhadas entre threads
atributos são compartilhados entre threads,
compartilhamento de recursos entre threads é fácil, mas entre processsos é dificil
self.atributos compartilhados entre as threads


-----Compartilhamentos de circuitos-----
Lock - condição mutualmente exclusiva, seção crítica é onde modifica a variavel compartilhada. Essa ferramenta garante que quandohouver 2 threads querendo operar um att 
compartilhado uma espera a outra terminar a operação, evitando a corrupção da variavel. self.lock.acquire() ----thread executada 1 por 1---- self.lock.release
Semaforo - escolho quantas threads em paralelo posso ter,  serve para limitar recursos o lock é só uma por uma (segurança da boate - limita a quantidade de threads executadas)
