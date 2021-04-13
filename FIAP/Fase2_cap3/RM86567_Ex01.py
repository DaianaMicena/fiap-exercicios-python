from datetime import date

print("=-="*9)
print('    CONTROLE DE CALORIAS')
print("=-="*9)

resposta = ''
calorias = 0
dia = date.today().day

while resposta != "S":
    alimento = str(input(" 1 - Adicione o alimento consumido hoje: "))
    calorias = float(input(f" 2 - Quantas calorias o {alimento} alimento possui? "))
    calorias += calorias
    resposta = str(input("Deseja sair? [S] ou [N]?")).upper()


print(f'O total de calorias ingerida no dia {dia}/4/2021 foi de {calorias}')

