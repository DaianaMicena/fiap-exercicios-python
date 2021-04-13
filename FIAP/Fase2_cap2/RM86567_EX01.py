#calculo IMC

nome = str(input("Informe o seu nome: "))
peso = float(input(f"Olá {nome}, por gentileza, informe o seu peso: "))
altura = float(input(f"{nome}, por gentileza, informe a sua altura: "))

imc = round(peso / (altura * altura), 2)

print(f"Seu IMC é {imc}.")

if imc < 16.00:
    print("Seu peso é considerado:\033[1;31m Baixo peso Grau III. Procure auxílio médico.\033[m")
elif imc > 16.00 and imc < 16.99:
    print("Seu peso é considerado:\033[1;31m Baixo peso Grau II. Procure auxílio médico.\033[m")
elif imc > 17.00 and imc < 18.49:
    print("Seu peso é considerado:\033[1;31m Baixo peso Grau I. Procure auxílio médico.\033[m")
elif imc > 18.50 and imc < 24.99:
    print("Seu peso é considerado:\033[1;34m Peso Ideal! Parabéns, continue se cuidando!\033[m")
elif imc > 25.00 and imc < 29.99:
    print("Seu peso é considerado:\033[1;31m Sobrepeso. Procure auxílio médico.\033[m")
elif imc > 30.00 and imc < 34.99:
    print("Seu peso é considerado:\033[1;31m Obesidade Grau I. Procure auxílio médico.\033[m")
elif imc > 35.00 and imc < 39.99:
    print("Seu peso é considerado:\033[1;31m Obesidade Grau II. Procure auxílio médico.\033[m")
else:
    print("Considerado:\033[1;31m Obesidade Grau III. Procure auxílio médico.\033[m")
