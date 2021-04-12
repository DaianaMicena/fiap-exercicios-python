#entrada
altura = float(input("Informe sua altura"))
sexo = input("Informe seu sexo")
#processamento
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo nao reconhecido")
print (f"Seu peso ideal é {round(peso_ideal,2)}")
