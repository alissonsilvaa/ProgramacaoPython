'''Dada a atual crise hídrica do país, as pessoas começaram a construir
reservatórios para armazenar água em suas propriedades. Faça um
programa em linguagem Python que auxilie os utilizadores do reservatório a
controlarem seu consumo. Obtenha do teclado as dimensões de um
reservatório (altura, largura e comprimento, em centímetros) e o consumo
médio diário dos utilizadores do reservatório (em litros/dia).
Assuma que o reservatório esteja cheio, tenha formato cúbico e informe:
(a) A capacidade total do reservatório, em litros;
(b) A autonomia do reservatório, em dias;
(c) A classificação do consumo, de acordo com a quantidade de dias de
autonomia: Consumo elevado, se a autonomia for menor que 2 dias;
Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo
reduzido, se a autonomia maior que 7 dias.
Obs.: Considere que cada litro equivale a 1000 cm3 ou 1 dm3 .'''

altura = float(input("Informe a altura do reservatório: "))
largura = float(input("Informe a largura do reservatório: "))
comprimento = float(input("Informe o comprimento do reservatório "))
qtdPessoas = int(input("Informe a quantidade de pessoas: "))

areaTotal = largura * comprimento * altura

if areaTotal > 0:
  print("A capacidade é de:",areaTotal,
        "A autonomia do reservatório é de",(areaTotal / 2 ) * qtdPessoas
         )