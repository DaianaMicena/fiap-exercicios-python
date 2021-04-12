frase = input('Insira a frase: ')
new = frase.lstrip().rstrip().lower().replace(" ","")



aux = new[::-1]

print(aux)

#print(f'O inverso de {frase} é {aux}')

#if new == aux:
 #   print(f'A frase {frase} é palindromo. ')
#else:
 #   print(f'A frase {frase} nao é palindromo. ')

