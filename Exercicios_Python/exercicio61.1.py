cont = 1

print('=======================')
print(' 10 TERMOS DE UMA P.A ')
print('=======================')

primeirotermo = int(input('Digite o primeiro termo:'))
razao = int(input("Digite a razao: "))
termo = primeirotermo
while cont <= 10:
    print(f"{termo} -> ", end=" ")
    cont +=1
    termo += razao
print("FIM!")