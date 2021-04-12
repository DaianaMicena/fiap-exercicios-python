from datetime import datetime


def verificaidade(data):
#data = int(input('Informe seu ano nascimento: '))
    print(f'Ano de nascimento: {data}.')

    currentYear = datetime.now().year
    idade = currentYear - data
    dif = idade - 18
    alis = data + 18

    print(f'Quem nasceu em {data} tem \033[33m {idade} anos\033[m em {currentYear}.')

    if idade < 18:
        return [0, dif]
    elif idade == 18:
        return [1, dif]
    else:
        return [2, dif, alis]


def output(ano):
    result = verificaidade(ano)
    if result[0] == 0:
        return f'Você não tem idade para se alistar, faltam \033[31m{result[1]} anos.\033[m'
    elif result[0] == 1:
        return 'Você deve se alistar \033[1;30;44m IMEDIATAMENTO!!! \033[m.'
    return f'Você já deveria ter se alistado há \033[31m{result[1]} anos.\033[m' + f'\nSeu alistamento foi em \033[31m {result[2]}. \033[m'


if __name__ =='__main__':
    result = output(2000)
    print(result)





