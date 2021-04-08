#desconto
#FiapWear

valor = float(input("Informe o valor da roupa: "))
cupom = input("Informe o cupom de desconto: ").upper()
valor_final = valor * 0.9

if cupom == 'CUPOM10':
    print(f"Valor final da compra é R$ {round(valor_final,2)}")
else:
    print("CUPOM INVÁLIDO!")
    print(f"Valor final da compra {valor}")





