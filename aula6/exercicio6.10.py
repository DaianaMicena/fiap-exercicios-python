#entrada
idade = int(input("Informe a idade"))
#processamento
if idade >= 5 and idade <= 7:
    print(f"Criancas com idade de {idade} anos fara parte da categoria Infantil A")
elif idade >= 8 and idade <= 11:
    print(f"Criancas com idade de {idade} anos fara parte da categoria Infantil B")
elif idade >=12 and idade <= 13:
    print(f"Criancas com idade de {idade} anos fara parte da categoria Juvenil A")
elif idade >= 14 and idade <= 17:
    print(f"Criancas com idade de {idade} anos fara parte da categoria Juvenil B")
elif idade >= 18:
    print(f"Adultos com idade de {idade} anos fara parte da categoria Adultos")


