# inicialização da Variaveis #Global
choice = 0

# Entrada de dados
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

# Processamento
while choice != 5:
    print("========== MENU ===========")
    print("[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa")

    choice = int(input("Escolha uma ação: "))

    if choice == 1:
        print(f"O valor da soma de {n1} e {n2} é {n1 + n2}. ")

    if choice == 2:
        print(f"O valor da multiplicação de {n1} e {n2} é {n1 * n2}. ")

    if choice == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        else:
            print(f' O maior valor é {n2}')

    if choice == 4:
        print('Digite os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    if choice == 5:
        print('Finalizando...')

print('Acabou, Obrigada!!!')




