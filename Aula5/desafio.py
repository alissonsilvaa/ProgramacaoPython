# Definir o número escolhido pelo usuário
numero = int(input("Digite um número para praticar a tabuada: "))

# Definir a variável para contar os acertos
acertos = 0

# Loop para iterar de 1 a 10
for i in range(1, 11):
    # Apresentando a operação de multiplicação
    print(f"{numero} x {i} = ?")

    # Resposta do usuário
    resposta = int(input())

    # Verificando se a resposta está correta
    if resposta == numero * i:
        # Incrementando o contador de acertos
        acertos += 1
        print("Resposta correta!")
    else:
        print(f"Resposta incorreta. A resposta correta é {numero * i}.")

# Apresentando o resultado final
print(f"Você acertou {acertos} de 10 perguntas.")

# Mensagem final de incentivo
if acertos == 10:
    print("Parabéns! Você dominou a tabuada do número", numero, "!")
else:
    print("Continue praticando para melhorar seu desempenho!")