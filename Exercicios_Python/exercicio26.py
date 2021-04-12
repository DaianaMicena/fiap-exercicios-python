frase = str(input('Digite uma frase')).upper()
qnt = frase.count('A')
print(f'A quantidade da letra A que aparece é {qnt}')

primeiro = frase.find('A')
print(f'A primeira letra A aparece na {primeiro} posição')

ultima = frase.rfind('A')
print(f'A ultima letra A aparece na {ultima} posição')
