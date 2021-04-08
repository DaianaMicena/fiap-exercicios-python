#Assinatura

nome = str(input("Informe o seu nome: "))
plano = str(input(f"Olá Sr.(a) {nome}, por gentileza, informe a sua assinatura: "))
if plano != "basic" and plano != "silver" and plano != "gold" and plano != "platinum":
    print(f"O plano: {plano} não existe.")
    exit()
faturamento = float(input("Informe seu faturamento anual:R$  "))

if plano == 'basic':
    bonusI = faturamento * 0.3
    print(f"O valor do bônus a ser pago será de R$ {round(bonusI,2)}")
elif plano == 'silver':
    bonusII = faturamento * 0.2
    print(f"O valor do bônus a ser pago será de {round(bonusII,2)}")
elif plano == 'gold':
    bonusIII = faturamento * 0.1
    print(f"O valor do bônus a ser pago será de {round(bonusIII,2)}")
elif plano == 'platinum':
    bonusIV = faturamento * 0.05
    print(f"O valor do bônus a ser pago será de {round(bonusIV,2)}")