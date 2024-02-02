
print("Hello World!!!")

--------------------x-------------------------------------

valor_uni = float(input("Informe o valor do produto: "))
quantidade = int(input("Informe a quantidade: "))
print("O valor do produto é:",valor_uni*quantidade)

--------------------x--------------------------------------

'''Crie um programa para entrar com a base a altura de um retângulo
e imprimir respectivamente o perímetro e a área correspondente.'''

area = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
print("O perímetro do retângulo é:",(area + altura)*2 )
print("A área do retângulo é: ",format((area * altura),".2f"))

-----------------------x----------------------------------

'''Crie um programa que dados o valor, a taxa e
o tempo, efetuar o cálculo do valor de
uma prestação em atraso, utilizando a fórmula:
prestação = valor + (valor * (taxa/100) * tempo)
'''
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa: "))
tempo = int(input("Digite a os dias em atraso: "))
prestacao = valor + (valor *(taxa/100) * tempo)
print("O Valor da prestação é: ", format(prestacao, ".2f"))