vetor = []
maiores_de50 = False

for n in range (0,5):
    num = int(input(f"Informe um numero {n+1} de 5: "))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print(f"Numero {n} maior que 50 na posicao {(vetor.index(n))}")
        maiores_de50 = True
    if maiores_de50 == False:
        print("Nao ha numeros maiores que 50")
