ano =  int(input('Digite um ano'))

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[33;m{ano}\033[m é bissexto.')
else:
    print(f'O ano \033[33;m{ano}\033[m nao é bissexto.')