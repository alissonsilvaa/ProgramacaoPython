'''Dada uma lista L de n valores inteiros, escreva
um programa que remova os números pares da lista'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_impares = []


for numero in L:

  if numero % 2 != 0:
    lista_impares.append(numero)


print(lista_impares)