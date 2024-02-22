'''Escreva um programa que compare duas listas. Considere a primeira lista como 
a versão inicial e a segunda como a versão após alterações. Utilizando operações
 com conjuntos, seu programa deverá imprimir a lista de modificações entre essas
  duas versões, listando:
• os elementos que não mudaram
• os novos elementos
• os elementos que foram removidos'''

def comparar_listas(lista_inicial, lista_final):
  """
  Compara duas listas e imprime as modificações entre elas.

  Argumentos:
    lista_inicial (list): A lista inicial.
    lista_final (list): A lista final.

  Retorna:
    None.
  """

 
  conjunto_inicial = set(lista_inicial)
  conjunto_final = set(lista_final)

  nao_mudaram = conjunto_inicial & conjunto_final

  
  novos_elementos = conjunto_final - conjunto_inicial

 
  elementos_removidos = conjunto_inicial - conjunto_final


  print("Elementos que não mudaram:", nao_mudaram)
  print("Novos elementos:", novos_elementos)
  print("Elementos removidos:", elementos_removidos)


lista_inicial = ["a", "b", "c", "d", "e"]
lista_final = ["a", "c", "e", "f", "g"]

comparar_listas(lista_inicial, lista_final)