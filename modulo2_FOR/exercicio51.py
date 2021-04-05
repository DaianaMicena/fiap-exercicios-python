cont = 0


primeirotermo = int(input('Informe um numero: '))
razao = int(input('Informe a razao: '))
n = int(input('Quantos elementos mostrar? '))

ultimo = primeirotermo + (n-1) * razao
ultimo = ultimo + 1

print('=======================')
print(' 10 TERMOS DE UMA P.A ')
print('=======================')

for p in range(primeirotermo, ultimo, razao):
    cont += 1
    if cont <=10:
        print(p)