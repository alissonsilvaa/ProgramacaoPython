'''Dadas duas lista P1 e P2, ambas com n valores reais que represetam as
notas de uma turma na prova 1 e na prova 2, respectivamente, escreva um
programa que calcule a média da turma nas provas 1 e 2, imprimindo em
qual das provas a turma obteve a melhor média'''

P1 = [8.5, 7.0, 9.5, 6.0, 10.0]
P2 = [9.0, 8.0, 8.5, 7.0, 9.5]

soma_p1 = 0
soma_p2 = 0

for nota in P1:
  soma_p1 += nota

for nota in P2:
  soma_p2 += nota

media_p1 = soma_p1 / len(P1)

media_p2 = soma_p2 / len(P2)

media_p1_arredondada = int(media_p1 * 100) / 100
media_p2_arredondada = int(media_p2 * 100) / 100

print(f"Média da prova 1: {media_p1_arredondada}")
print(f"Média da prova 2: {media_p2_arredondada}")

if media_p1 > media_p2:
  print("A turma obteve a melhor média na prova 1.")
elif media_p1 < media_p2:
  print("A turma obteve a melhor média na prova 2.")
else:
  print("A turma obteve a mesma média nas duas provas.")