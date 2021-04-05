from random import randint
from time import sleep

print('Vou pensar um numero, tente adivinhar...')

sorteio = (randint(0,5))

digite = int(input('Digite um numero '))

print('PROCESSANDO...')
sleep(5)

if digite == sorteio:
    print('Parabens, voce ganhou!')
else:
    print(f'Desculpe, eu pensei no número {sorteio} e nao no número {digite}, tente outra vez!')

