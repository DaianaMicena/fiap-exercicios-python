vetor = []

codigo = int(input("Informe o codigo: "))
if codigo != 0:
    for n in range (0,5):
    codigo = int(input(f"Digite um numero {n+1} de 5: "))
    vetor.append(n)
    for n in vetor:
    if n  == 1:
        print(f" O vetor é {(vetor.count(n))}")
    if num == 2:
        vetor.reverse
