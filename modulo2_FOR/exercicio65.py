

soma = 0
c = 0
lista = []
media = 0


num = int(input('Digite um numero:'))
pergunta = str(input('Quer continuar? [S/N]'))

while pergunta != 'N':
    soma += num
    c += 1
    num = int(input('Digite um numero:'))
    pergunta = str(input('Quer continuar? [S/N]'))
    lista.append(num)

print(f'Os numeros foram digitados {c} vezes, a media foi de {soma} / {c}.')
print(f'O maior numero foi {max(num)}e o menor {min(num)}foi.')






