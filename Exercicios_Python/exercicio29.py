veloc = float(input('Informe a velocidade registrada '))

excedente = veloc - 80

multa = excedente * 7.00

if veloc >= 80:
    print(f'\033[31mMULTADO! O Sr ultrapassou o limite de 80 km/h.\033[m \nO Sr(a) será multado no valor de R$ {round(multa,2)}.')
else:
    print('Parabens, o sr(a) respeitou as leis de transito.')

print('Tenha um bom dia e dirija com segurança.')




