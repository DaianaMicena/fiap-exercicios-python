from datetime import date
atual = date.today().year

nasc = int(input('Qual seu ano de nascimento?'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos')

if idade == 18:
    print('Voce precisa se alistar \033[30;41m IMEDIATAMENTE!!! \033[m')

elif idade < 18:
    saldo = 18 - idade
    alis = saldo + atual
    print(f' Faltam \033[30;41m {saldo} anos \033[m para voce se alistar. Seu alistamento sera em {alis}.')

elif idade > 18:
    saldo =  idade -18
    alis = atual - saldo
    print(f'O seu alistamento foi há {saldo} anos, no ano de {alis}.')