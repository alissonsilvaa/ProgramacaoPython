'''Faça um programa que permita ao usuário digitar o seu nome e em seguida 
mostre o nome do usuário de trás para frente utilizando comente letras 
maiúsculas. Dica: lembre-se que ao informar o nome o usuário pode digitar 
letras maiúsculas.'''

nome = input("Digite seu nome: ").upper()
lista = []

for letra in nome:
  lista.append(letra)

lista.reverse()
nome_invertido = ''.join(lista)

print(nome_invertido)
