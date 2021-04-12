n1 = float(input('Digite sua primeira nota: '))
n2 =  float(input('Digite sua segunda nota: '))
media = (n1+n2) / 2

print(f'Tirando {n1} e {n2}, a média é {media}.')

if media < 5:
    print('\033[31;40m O aluno está REPROVADO\033[m')
elif media > 5 < 6.9:
    print('\033[33;40m O aluno está em RECUPERACAO \033[m')
elif media > 7:
    print('\033[34;40m O aluno está APROVADO \033[m')
