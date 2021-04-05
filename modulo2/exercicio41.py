from datetime import date
atual = date.today().year

ano = int(input('Informe seu ano de nascimento: '))
#print(ano)

saldo = atual - ano

print(f'O atleta tem {saldo} anos.')


if saldo <= 9 :
   print('Classificação: \033[35mMIRIM\033[m.')
elif saldo > 9 and saldo <= 14 :
    print('Classificação: \033[35mINFANTIL \033[m')
elif saldo > 14 and saldo <= 19 :
    print('Classificação: \033[35mJUNIOR \033[m')
elif saldo > 19 and saldo <=20 :
    print('Classificação: \033[35mSENIOR \033[m')
else:
    print('Classificação: \033[35mMASTER \033[m')



