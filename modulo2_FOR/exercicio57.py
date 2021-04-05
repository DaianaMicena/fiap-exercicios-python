

sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo [F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso.')
