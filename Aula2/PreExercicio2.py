'''Faça um programa que peça dois números ao usuário e mostre 
qual o maior e qual o menor.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
  print("O número maior é ",num1,"e o menor é",num2)

elif num1 < num2:
  print("O número maior é ",num2,"e o menor é",num1 )

else:
  print("Opçao inválida")
