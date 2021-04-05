#entrada
numero = int(input("Informe um numero"))
#processamento
if numero % 2 == 0:
    if numero > 0:
        print(f"O numero {numero} é par e positivo")
    else:
        if numero < 0:
            print(f"O numero {numero} é par e negativo")
else:
    if numero < 0:
        print(f"O numero {numero} é impar e negativo")
    else:
        print(f"O numero {numero} é impar e positivo")