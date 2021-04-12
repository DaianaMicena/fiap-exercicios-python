peso = float(input('Informe o seu peso: '))
altura =  float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)

print(f'O seu IMC é {round(imc,1)}',end= '')

if imc < 18.5:
    print(' \033[30;41mVoce esta abaixo do peso.\033[m')
elif 18.5 <= imc < 25:
    print(' \033[30;44mParabéns! Voce esta com peso ideal.\033[m')
elif 25  <= imc < 30:
    print(' \033[30;43mVoce esta com sobrepeso.\033[m')
elif 30 <= imc < 40:
    print(' \033[30;41mVoce esta com obesidade.\033[m')
else:
    print(' \033[31;40mVoce esta com obesidade morbida.\033[m')

#abaixo de 18.5 = Abaixo do peso
# 25 =  Peso ideal
# 30 = Sobrepeso
# 40 =  Obesidade
# Acima de 40 =  Obesidade Morbida
