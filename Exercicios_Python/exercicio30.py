num = int(input('Digite um numero'))

if num % 2 ==0:
    print(f'\033[31;m O numero {num} é par.\033[m')
else:
    print(f'\033[34;mO numero {num} é impar.\033[m')