
'''Um banco concederá um crédito especial aos seus clientes, variável com o saldo
médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule
o valor do crédito de acordo com a tabela abaixo. Mostre uma mensagem informando
o saldo médio e o valor do crédito. (use o comando caso-de e não faça repetições)'''

saldo = int(input('''|Saldo médio |Percentual                 |
                     __________________________________________
                     |de 0 a 200  |nenhum crédito             |
                     |de 201 a 400|20% do valor do saldo médio|
                     |de 401 a 600|30% do valor do saldo médio|
                     |acima de 600|40% do valor do saldo médio|

Digite o saldo médio do cliente:
'''))

if saldo < 200:
  print("O Saldo de",saldo,"não tem crédito!")

elif saldo > 200 and saldo <= 400:
  print("O valor do saldo",saldo * 0.2)

elif saldo > 400 and saldo <=600:
  print("O valor do saldo",saldo * 0.3)

elif saldo > 600:
  print("O valor do saldo",saldo * 0.4)

else:
  print("Opção inválida!")