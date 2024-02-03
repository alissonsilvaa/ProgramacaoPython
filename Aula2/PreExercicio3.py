'''Escreva um programa em Python que 
recebe um inteiro e diga se é par ou ímpar.'''

entrada = int(input("Digite um número: "))

if entrada %2 == 0:
  print("O número",entrada,"é par!")

elif entrada %2 != 0:
  print("O número",entrada,"é ímpar")