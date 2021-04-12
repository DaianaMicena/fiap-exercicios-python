from random import randint

tentativa = 0

print('Vou pensar em um numero, tente adivinhar...')

computador = (randint(0,10))

acertou = False

while not acertou:
    digite = int(input('Informe um numero'))
    tentativa += 1
    if digite == computador:
        print(f' Parabens voce acertou na {tentativa} ª tentativa!!!')
    if digite > computador:
        digite = int(input('Errou, mais para baixo:'))
    if digite < computador:
        digite = int(input('Errou, mais para cima:'))



