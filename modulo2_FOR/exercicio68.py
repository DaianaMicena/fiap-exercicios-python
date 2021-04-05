from random import randint

ganhar = True
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

while ganhar:
    aposta = int(input('Qual seu número?'))
    escolha = str(input('Voce quer par ou ímpar?'))
    computador = randint(1,10)

    total = aposta + computador

    if total % 2 == 0:
        result = 'par'
        print (f'Voce jogou {aposta} e o computador {computador}. Total {total} deu PAR. ')
    else:
        result = 'impar'
        print(f'Voce jogou {aposta} e o computador {computador}. Total {total} deu ÍMPAR. ')
    if escolha == result:
        print('Voce GANHOU!!!')
    else:
        ganhar = False
        print('Voce PERDEU!!!')