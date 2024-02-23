'''Faça um programa que leia 2 strings e informe o conteúdo delas seguido
do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
e são iguais ou diferentes no conteúdo.'''

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

print("String 1:", str1, "Comprimento:", len(str1))
print("String 2:", str2, "Comprimento:", len(str2))

if len(str1) == len(str2):
    print("As duas strings possuem o mesmo comprimento.")
else:
    print("As duas strings possuem comprimentos diferentes.")

if str1 == str2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdos diferentes.")

if str1.startswith(str2):
    print("A segunda string começa com a primeira string.")
else:
    print("A segunda string não começa com a primeira string.")