
totalidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0
somaidade = 0


for d in range(1,4):
    print(f'============== Dados das {d}ª pessoa ============= ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
    if d == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade > 20:
        totalmulher += 1

mediaidade = somaidade / d
print(f'A media das idades é {mediaidade}')
print(f'O nome do homem mais velho tem {maioridadehomem} é {nomevelho}')
print(f'O total de mulher acima de 20 anos é {totalmulher}')





