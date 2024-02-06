'''Desenvolva um programa que recebe do usuário, o placar de um
jogo de futebol (os gols de cada time) e informa se o resultado
foi um empate, se a vitória foi do primeiro time ou do segundo time.'''

timeA = int(input("Gols do time da casa: "))
timeB = int(input("Gols do time visitante: "))

if timeA == timeB:
  print("O resultado foi empate: ",timeA,"x",timeB)

elif timeA > timeB:
  print("O time da casa venceu por: ",timeA,"x",timeB)

else:
  print("O time visitante venceu por: ",timeB,"x",timeA)
