from decimal import Decimal

nome = input('Por gentileza, informe seu nome: ')
print((f'Olá {nome},') ,end=' ')


renda = float(input('informe seu salário: R$ '))
valor = float(input('Agora preciso que informe o valor da casa: R$ '))
qnt = float(input(f'{nome}, em quantos anos gostaria de pagar? '))

parcela = (valor / qnt) / 12

regra = renda * 30 /100


print(f'O valor da parcela é R$ {round(Decimal(parcela),2)}')

if parcela > regra:
    print(f'\033[31m FINANCIAMENTO NEGADO!\033[m Valor excede os 30% do seu salário.')
else:
    print(f'\033[32m Parabéns, financiamento aprovado!\033[m')


