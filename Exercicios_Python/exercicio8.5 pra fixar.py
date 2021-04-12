vetor = []
maiores_50 = False

for n in range (0,5):
    num = int(input(f"Informe um numero {n+1} de 5 "))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print(f"Numero {n} maior que 50 na posiçao {(vetor.index(n))}")
        maiores_50 = True
    if maiores_50 == False:
        print("Nao há numeros maiores que 50")

