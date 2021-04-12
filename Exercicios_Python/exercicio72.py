escolha = 0

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input(' Digite um numero de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
    print ('Tente novamente', end='' )
print(f'O numero que voce digitou foi {num[escolha]}.')
