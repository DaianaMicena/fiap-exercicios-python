maior = 0
empate = ''

segunda = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às segundas-feiras? "))
terca = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às terças-feiras? "))
quarta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às quartas-feiras? "))
quinta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às quintas-feiras? "))
sexta = int(input("Informe a quantidade de votos recebidos para que a live seja transmitida às sextas-feiras? "))

# votos = {"segunda": segunda,
#  "terça": terca,
#  "quarta": quarta,
#  "quinta": quinta,
#  "sexta": sexta
#  }

# for k, v in votos.items():
#     if maior < v:
#         maior = v
#         dia = k
# print(f"o dia {dia} teve {maior} votos")
#
if maior < segunda:
    dia = 'segunda'
    maior = segunda
    dia_anterior = dia
if maior == terca:
     dia = 'terça'
     empate = f'{dia} é igual {dia_anterior}'
if maior < terca:
    dia = 'terca'
    maior = terca
    dia_anterior = dia

if maior == quarta:
    dia = 'quarta'
    empate = f'{dia} é igual {dia_anterior}'
if maior < quarta:
    dia = 'quarta'
    maior = quarta
if maior == quinta:
    dia = 'quinta'
    empate = f'{dia} é igual {dia_anterior}'
if maior < quinta:
    dia = 'quinta'
    maior = quinta
if maior == sexta:
    dia = 'sexta'
    empate = f'{dia} é igual {dia_anterior}'
if maior < sexta:
    dia = 'sexta'
    maior = sexta

if empate:
    print(empate)
else:
  print(f'O dia {dia} recebeu {maior}')



# if maior < terca:
#     maior = terca
#     dia = 'terca'
#
# if maior < quarta:
#     maior = quarta
#     dia = 'quarta'
#
# if maior < quinta:
#     maior = quinta
#     dia = 'quinta'
#
# if maior < sexta:
#     maior = sexta
#     dia = 'sexta'
#print(f'O dia {dia} recebeu {maior}')


#soma_votos += segunda, terca, quarta, quinta, sexta

#print(f"O dia mais votado foi {mais_votos}.")
#print(f"A quantidade de votos no total foram {soma_votos}")