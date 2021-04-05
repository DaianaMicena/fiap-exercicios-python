vetor = []

for n in range (0,5):
    num = int(input(f"Digite um numero {n+1} / 5: "))
    vetor.append(num)

print(f"A soma do vetor é {(sum(vetor))}")