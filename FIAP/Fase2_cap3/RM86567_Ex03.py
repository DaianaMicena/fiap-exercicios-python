print("=-="*9)
print('   SEQUENCIA DE FIBONATTI')
print("=-="*9)

n1 = 0
n2 = 1
count = 0
result = 0
termo = int(input("Informe um número: "))

if termo <= 0:
    print(f"Número {termo} é inválido")

while count < termo:
    fib = n1 + n2

    n1 = n2
    n2 = fib
    count += 1

    if termo == fib:
        print('Açao bem sucedida!')
        result = fib

if result != termo:
    print('Acão falhou...')




