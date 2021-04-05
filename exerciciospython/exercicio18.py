import math
angulo = float(input('Digite um angulo'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O seno do angulo {angulo} é {round(sen,2)}, o cosseno é {round(cos,2)} e a tangente é {round(tan,2)}')