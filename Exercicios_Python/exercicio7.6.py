#entrada
numero = int(input("Informe um numero entre 1 e 10"))
#processamento
while numero < 1 or numero > 10:
    numero = int(input("Informe um numero entre 1 e 10:"))
print(f"A tabuada de {numero}")
for n in range (1, 11):
    print(f"{numero}*{n} = {numero * n}")
