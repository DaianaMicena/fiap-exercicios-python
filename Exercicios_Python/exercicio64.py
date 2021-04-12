

c = 0
new =0
#n = 0

n = int(input('Digite um numero: [999] para SAIR! '))
while n != 999:
    new += n
    c += 1
    n = int(input('Digite um numero: [999] para SAIR! '))

print(f'O total de vezes digitada foram {c} e a soma total é de {new} .')
print("FIM!")


