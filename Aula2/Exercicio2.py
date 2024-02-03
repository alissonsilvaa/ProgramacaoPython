'''Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino
e ?F? feminino), construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:

- para homens: (72.7*h)-58
- para mulheres: (62.1*h)-44.7'''

sexo = (input('''Digite seu sexo:
                    M- Homem
                    F- Mulher
                  '''))

altura = float(input("Digite sua altura: "))
imcHomem = (72.7 * altura)-58
imcMulher = (62.1 * altura)-44.7

if sexo == "M":
  print("Seu IMC é de:",format(imcHomem,".2f"))

elif sexo == "F":
  print("Seu IMC é de:",format(imcMulher,".2f"))

else:
  print("Opção inválida!")