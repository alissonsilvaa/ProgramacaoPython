'''Faça um programa em Python (utilize a estrutura for)
que leia 10 valores inteiros e:
Encontre e mostre o maior valor
Encontre e mostre o menor valor
Calcule e mostre a média dos números lidos'''

maior = 0
menor = 0
soma = 0

# Loop para ler os 10 valores
for i in range(10): # Lembre-se de que na range equivale a (inicio, controle,pulos)

  valor = int(input("Digite um valor: "))

  # Atualização do maior valor
  if valor > maior:
    maior = valor

  # Atualização do menor valor
  if valor < menor or i == 0:
    menor = valor

  # Acumulação da soma
  soma += valor

# Cálculo da média
media = soma / 10

# Apresentação dos resultados
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média: {media}")