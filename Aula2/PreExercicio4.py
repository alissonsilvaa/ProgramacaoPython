'''Escreva um programa que pergunte o ano de nascimento
 de uma pessoa e diga se ele é maior de idade'''

anoNascimento = int(input("Digite seu ano de nascimento: "))

if anoNascimento < 2006:
  print("Você é maior de idade!")

else:
  print("Você é menor de idade!