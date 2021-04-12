def calcula(compras, forma):
    ''''

    function calcula:
    param: numerico compras
    param: inteiro forma

    '''

    print('=============== LOJAS MICENAS ================')

    #compras  = float(input('Qual valor do compras? '))
    #forma = int(input('FORMA DE PAGAMENTO\n [ 1 ] à vista dinheiro / cheque \n [ 2 ] à vista no cartao\n [ 3 ] 2x no cartao \n [ 4 ] 3x ou mais no cartao'))

    # processamento de dados calculo do desconto e juros
    desccash = compras - (compras*10/100)
    desccard = compras - (compras*5/100)
    juros = compras + (compras*20/100)

    # condicão forma de pagamento
    if forma == 1:
        return(f'O valor para pagamento será de R$ {desccash}.')
    elif forma == 2:
        return(f'O valor para pagamento será de R$ {desccard}.')
    elif forma == 3:
        return(f'O valor para pagamento será de R$ {compras}')
    elif forma == 4:
        return(f'O valor para pagamento será de R$ {juros}')


if __name__ =='__main__':
    # chamada da funcão
    result = calcula(400.00,2)
    #print result
    print(result)


