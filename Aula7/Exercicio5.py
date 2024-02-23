''' programa que use a função valorPagamento para determinar o valor a ser pago
por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor
da prestação e o número de dias em atraso e passar estes valores para a função
valorPagamento, que calculará o valor a ser pago e devolverá este valor ao 
programa que a chamou. O programa deverá então exibir o valor a ser pago 
na tela. Após a execução o programa deverá voltar a pedir outro valor de 
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório 
do dia, que contará a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser paga é feito da seguinte forma. Para pagamentos sem 
atraso, obrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, 
mais 0,1% juros por dia de atraso.'''

def valorPagamento(valor_prestacao, dias_atraso):
    multa = 0.03  # 3% de multa em caso de atraso
    juros_diarios = 0.001  # 0.1% de juros por dia de atraso
    valor_a_pagar = 0
    
    if dias_atraso == 0:
        valor_a_pagar = valor_prestacao
    else:
        valor_a_pagar = valor_prestacao + (valor_prestacao * multa) + (valor_prestacao * juros_diarios * dias_atraso)
    
    return valor_a_pagar

total_prestacoes = 0
total_valor_pago = 0

while True:
    valor = input('''
                
    Digite o valor da prestação (ou '0' para encerrar): ''')
    if valor == '0':
        break
    
    dias_atraso = int(input("Digite o número de dias em atraso: "))
    
    valor = float(valor)
    valor_a_pagar = valorPagamento(valor, dias_atraso)
    
    print("Valor a ser pago: R$", valor_a_pagar)
    
    total_prestacoes += 1
    total_valor_pago += valor_a_pagar

print("\nRelatório do dia:")
print("Total de prestações pagas:", total_prestacoes)
print("Valor total pago:", total_valor_pago)
