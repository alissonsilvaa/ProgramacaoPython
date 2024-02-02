
'''Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o
valor a ser pago por aquele lanche. Considere que a cada execução somente será
calculado um item.'''
programa = int(input('''Digite a opção desejada:
             |Especificação   |Código| Preço
             _________________|______|_______
             |Cachorro quente |100   | 1,20
             |Bauru simples   |101   | 1,30
             |Bauru com ovo   |102   | 1,50
             |Hambúrger       |103   | 1,20
             |Cheeseburguer   |104   | 1,30
             |Refrigerante    |105   | 1,00
              '''
              ))
quantidade = int(input("Agora digite a quantidade: "))

if programa == 100:
  print("Total a pagar:",format(quantidade * 1.20,".2f"))

elif programa == 101:
  print("Total a pagar:",format( quantidade * 1.30,".2f"))

elif programa == 102:
  print("Total a pagar:",format( quantidade * 1.50,".2f"))

elif programa == 103:
  print("Total a pagar:",format( quantidade * 1.20,".2f"))

elif programa == 104:
  print("Total a pagar:",format( quantidade * 1.30,".2f"))

elif programa == 105:
  print("Total a pagar:",format( quantidade * 1.00,".2f"))

else:
  print("Opção inválida!")

-----------------------------------x-----------------------------------------

'''Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino
e ?F? feminino), construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:

- para homens: (72.7*h)-58
- para mulheres: (62.1*h)-44.7'''

imc = int(input('''Digite seu sexo:
                    1- Homem
                    2- Mulher
                  '''))

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))