from random import randint
from time import sleep
tentativa = 1

print('Vou pensar em um numero, tente adivinhar...')

sorteio = (randint(0,10))

digite = int(input('Digite um numero '))

#print('PROCESSANDO...')
#sleep(5)

while digite != sorteio:
    digite = int(input('Errado! Tente novamente: '))
    tentativa += 1
print(f'Parabens, voce acertou na {tentativa} ª tentativa!')
