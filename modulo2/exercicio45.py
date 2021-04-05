
import sys
import random

print('============ GAME =============')
print('Suas opcões: \n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 } TESOURA\n')


itens = ('PEDRA','PAPEL','TESOURA')
computador = random.randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))


if jogador not in computador:
    sys.exit('Numero inválido')


maquina = random.choice(itens[computador])

print(f'O numero  escolhido pela maquina foi {maquina}.')











if jogador == maquina:
    print('Nao houve ganhador, Tente novamente!')
elif jogador == 0 and maquina == 1 or jogador == 1 and maquina == 2 or jogador == 2 and maquina == 0:
    print('Vocë perdeu!')
else:
    print('Voce ganhou!')






