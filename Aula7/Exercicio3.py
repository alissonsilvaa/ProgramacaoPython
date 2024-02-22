'''faça um programa, com uma função que necessite de um argumeto. A função 
retorna o valor de caractere 'P', se seu argumento for positivo, 
e 'N' se seu argumento for zero ou negativo.'''

lambda_positivo_negativo = lambda x: 'P' if x > 0 else 'N'

print(lambda_positivo_negativo(1))
print(lambda_positivo_negativo(0))
print(lambda_positivo_negativo(-1))