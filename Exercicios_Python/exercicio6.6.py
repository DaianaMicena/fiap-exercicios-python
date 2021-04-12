#variaveis
hora_trabalhada = 10.00
hora_excedente = 20.00
#entrada
quantidade_horas = float(input("Informe a quantidade de horas trabalhadas"))
#processament
limite = 50
if quantidade_horas > limite:
    valor_pagar_extra = (quantidade_horas - limite) * hora_excedente
    valor_pagar_total = (limite * hora_trabalhada) + valor_pagar_extra
    print(f"Valor total a pagar é R$ {valor_pagar_total}. \n Valor pago pelas horas extras é R$ {valor_pagar_extra}")
else:
    print(f"Valor total a pagar é R$ {hora_trabalhada * quantidade_horas}. \n Nao ha horas excedentes")


