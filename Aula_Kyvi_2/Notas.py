"""
Kivy é um framework do python orientado a eventos
Classe base app
Classe derivada para criar app em si
Linguagem disponibiliza separação da lógica (.py) e interface (.kv)
Size_hint e pos_hint, soma das alturas tem q ser 1, se colocarmos por exemplo size1 = 0.6 e size2 = 0.5 Kivy vai adequar para q a soma seja 1.
size_hint(width_proportion, height_proportion) = width e height são referentes ao pai 

Ex: 
  boxlayout(50%)
    -bt1
    -bt2 (25%)
  bt2 ocupa 12,5% da tela!!!

Box layout horizontal ignora a componente de altura deixando-a sempre 1
Box layout vertical ignora a componente de largura deixando-a sempre 1
pos_hint é um dicionário, só posso usar 2 das 6 chaves
x e y canto inferior direito
caso x, y = 1, compontente sai da tela, mas continua existindo

-----Modulo Clock-----
Componente que gera eventos temporizados
Clock.schedule_once(my_callback)
Quando tentamos trocar uma imagem com uma thread secundária ela fica preta, não é permitido trocar imagens em threads secundárias
Por isso utiliza-se o Clock.schedule_once(my_callback) (faz a chamada) na thread secundária e assim o my_callback é rodado na thread principal
"""
