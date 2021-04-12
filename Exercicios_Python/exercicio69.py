age = 0
total18= 0
homem = 0
mulher20 = 0
option = 0
sexo = 0

print('CADASTRE UMA PESSOA')
print ('=====================')
while True:
    age = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [F/M]'))
    print('----------------------------')
    if age > 18:
        #total18 = age
        total18 += 1
    if sexo == 'M':
        homem += 1
    if age > 20 and sexo == 'F':
        mulher20 += 1
    option = str(input('Quer continuar? [S/N]'))
    if option == 'N':
        break
print ('Finalizando cadastro')
print(f' {total18} pessoas com mais de 18 anos. ')
print (f' {homem} homens se cadastraram.')
print (f'{mulher20} Mulheres acima de 20 anos se cadastraram.')



