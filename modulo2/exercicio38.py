num = int(input('Digite um numero. '))
num2 = int(input('Digite um numero. '))

if num > num2:
    print(f'O PRIMEIRO numero \033[33m {num}\033[m é maior que o numero {num2}. ')
elif num2 > num:
    print(f'O SEGUNDO numero \033[33m {num2}\033[m é maior que o numero {num}. ')
else:
    print('Nao existe valor maior, os numeros sao iguais. ')

