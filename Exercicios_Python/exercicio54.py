from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for d in range(1,8):
    data = int(input(f'Informe o ano de nascimento da {d} pessoa:  '))
    saldo = atual - data
    if saldo < 21:
       totmenor +=1
    else:
        totmaior +=1
print(f'Tivemos {totmenor} menores de idade e {totmaior} maiores de idade. ')


