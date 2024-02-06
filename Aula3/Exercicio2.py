'''Faça um algoritmo que receba um valor de uma compra e
receba o numero de prestações, apresente o valor das
prestações sem juros.'''

valor = float(input("Qual o valor da compra? "))
prestacao = int(input("Em quantas parcelas? "))

prestaJuros = valor / prestacao

if valor > prestacao:
  print("O valor da parcela é de: ",prestaJuros)

elif prestacao > 10:
  print("O valor da prestação tem juros de 5%",prestaJuros * 0.50)

else:
  print("Valor invalido!")
