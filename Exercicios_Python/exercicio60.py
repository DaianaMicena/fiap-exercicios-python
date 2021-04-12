

n = int(input('Digite um numero: '))
f = 1
c = n
print(f'Calculando o fatorial de {n}! = ', end= '')
while c > 0:
    print(f'{c} ',end='')
    print(' x ' if c > 1 else '=' ,end ='' )
    f = f * c
    c = c - 1
print(f' {f} ')





#exercicio feito (1)

#fatorial = 1
#count = 1

#while count <= n:
 #   fatorial *= count
  #  count += 1
   # print (fatorial)

