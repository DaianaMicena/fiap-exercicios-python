
print('=======================')
print('   TERMOS DE UMA P.A   ')
print('=======================')

cont = 0
quant = 10
primeirotermo = int(input('Digite o primeiro termo:'))
razao = int(input("Digite a razao: "))
termo = primeirotermo

while cont < quant:
    print(f"{termo} -> ", end=" ")
    cont +=1
    termo += razao
    if cont == quant:
        new = int(input("Quantos termos voce quer a mais?: "))
        if new == 0:
            out = quant
        else:
            quant += new
print(f'A quantidade de termos informados foram {out}. \n FIM!!!')
