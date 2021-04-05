trecho = float(input('\033[34;mInforme a distancia da viagem:\033[m'))

valor = trecho * 0.50
valor2 = trecho * 0.45


#if trecho <=200:
 #   print(f'O valor a pagar é R$ {valor} ')
#else:
 #   print(f'O valor a pagar é R$ {valor2}')

#Forma mais rapida de fazer:

preço = trecho *0.50 if trecho <=200 else trecho * 0.45

print(f'O valora pagar pelo trecho é R$ {preço}.')