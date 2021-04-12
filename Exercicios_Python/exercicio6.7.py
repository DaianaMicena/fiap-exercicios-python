#entrada
numero1 = int(input("Informe um numero"))
numero2 = int(input("Informe um numero"))
numero3 = int(input("Informe um numero"))
numero4 = int(input("Informe um numero"))
#processamento
q1 = numero1 * numero1
q2 = numero2 * numero2
q3 = numero3 * numero3
q4 = numero4 * numero4

if q3 >= 1000:
    print(f"Numero 3 = {numero3} Quadrado = {q3}")
else:
    print(f" Numero 1 = {numero1} Quadrado = {q1}")
    print(f" Numero 2 = {numero2} Quadrado = {q2}")
    print(f" Numero 3 = {numero3} Quadrado = {q3}")
    print(f" Numero 4 = {numero4} Quadrado = {q4}")
