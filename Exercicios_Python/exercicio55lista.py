''''
# list var
pesos = []
for i in range(1, 6):
    # get weight person
    peso = float(input("Digite o seu peso: "))
    # append to list
    pesos.append(peso)
# print max value from the list
print(max(pesos))
# print min value from the list
print(min(pesos))
'''


def check_peso(pesos):
    return max(pesos), min(pesos)


if __name__ == '__main__':
    lista = [90.7, 85.8, 120.5, 60.5, 48.9]
    result = check_peso(lista)
    print(result)
