#Dia Escolhido para Live

maior = 0
total = 0

segunda = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às segundas-feiras? "))
terca = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às terças-feiras? "))
quarta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às quartas-feiras? "))
quinta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às quintas-feiras? "))
sexta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às sextas-feiras? "))

if maior < segunda:
     maior = segunda
     dia = 'segunda'

if maior < terca:
     maior = terca
     dia = 'terca'

if maior < quarta:
     maior = quarta
     dia = 'quarta'

if maior < quinta:
     maior = quinta
     dia = 'quinta'

if maior < sexta:
     maior = sexta
     dia = 'sexta'

total += segunda
total += terca
total += quarta
total += quinta
total += sexta

print(f"O dia da semana mais votado foi {dia}-feira com {maior} votos.")
print(f"O total de votos computados foi de {total}.")
