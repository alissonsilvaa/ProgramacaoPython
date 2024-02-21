def soma(n1, n2):
  soma = n1 + n2
  return soma

def subtracao  (n1, n2):
  sub = n1 - n2
  return sub

def multiplicacao (n1, n2):
  multi = n1 * n2
  return multi

def divisao (n1, n2):
  div = n1 / n2
  return div

print("Bem vindo a Calculadora")
num1 = int(input("Digite o primeiro numero: ")) 
num2 = int(input("Digite o segundo numero: "))

op = int(input('''Digite:
               1 - soma 
               2 - subtração
               3 - multiplicação
               4 - divisão
                  '''))

if op == 1:
  print("Valor da soma é",{soma(num1, num2)})
elif op == 2:
  print ("Valor da soma é:",{subtracao(num1, num2)})
elif op == 3:
  print("Valor da multiplicação é:", "{:.2f}".format(multiplicacao(num1, num2)))
elif op == 4:
  print("Valor da divisão é:",{divisao(num1, num2)})
else:
  print("comando Invalido! ")