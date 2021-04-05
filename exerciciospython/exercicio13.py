nome = input('informe o nome do funcionario ')
salario = float(input(f'informe o salario do {nome} R$ '))
reajuste = salario * 0.15
salarioatual = salario + reajuste
print(f'O salario atualizado do {nome} é R$ {round(salarioatual,2)}')
