#Batimentosporminuto

idade = 65 #int(input("Informe a idade: "))
batimentos = 65 #int(input("Informe os batimentos por minuto: "))

if idade <= 2 and (batimentos >= 120 and batimentos <= 140):
    print("Batimentos dentro da faixa adequada.")

elif idade <= 2 and batimentos < 120:
    print("Batimentos esta ABAIXO da faixa adequada.")

elif idade <= 2 and batimentos > 140:
    print("Batimentos esta ACIMA da faixa adequada.")

elif (idade >= 8 and idade <= 17) and (batimentos >= 80 and batimentos <= 100):
    print("Batimentos esta DENTRO da faixa adequada. linha 14")

elif (idade >= 8 and idade <= 17) and batimentos < 80:
    print("Batimentos esta ABAIXO da faixa adequada. linha 17")

elif (idade >= 8 and idade <= 17) and batimentos > 100:
    print("Batimentos esta ACIMA da faixa adequada. linha 18")

elif (idade >= 18 and idade <= 59) and (batimentos >= 70 and batimentos <= 80):
    print("Batimentos esta DENTRO da faixa adequada")

elif (idade >= 18 and idade <= 59) and (batimentos < 70):
    print("Batimentos esta ABAIXO da faixa adequada.")

elif (idade >= 18 and idade <= 59) and (batimentos > 80):
    print("Batimentos esta ACIMA da faixa adequada.")

elif idade > 60 and (batimentos >= 50 and batimentos <= 60):
    print("Batimentos esta DENTRO da faixa adequada.")

elif batimentos < 50:
    print("Batimentos esta ABAIXO da faixa adequada.")

elif batimentos > 60:
    print("Batimentos esta ACIMA da faixa adequada.")



