
# Variaveis
count_esfera = 0
count_limpeza = 0
count_conector = 0
count_inutilizado = 0
count_qtd = 0

# Entrada
identificacao = int(input("Informe o codigo de identificacao do mouse: ")) # Repetir essa rotina

# Processamento
# faça um while até que o valor da variavel seja != 0
while identificacao != 0:
    print (" 1 - Defeito na esfera")
    print (" 2 - Defeito na limpeza")
    print (" 3 - Defeito no conector")
    print (" 4 -  Inutilizado")

    defeito = int(input("Escolha o codigo do defeito: "))

    identificacao = int(input("Informe o codigo de identificacao do mouse: "))

# print das opções de defeito
# Tomada de decisão (if) qual var precisa atualizar
    if defeito == 1:
        count_esfera = count_esfera + 1
    elif defeito == 2:
        count_limpeza = count_limpeza + 1
    elif defeito == 3:
        count_conector = count_conector + 1
    elif defeito == 4:
        count_inutilizado = count_inutilizado + 1

count_qtd = count_conector + count_limpeza + count_inutilizado + count_esfera

print(f"Quantidade de mouses = {count_esfera + count_inutilizado + count_limpeza + count_conector}")
""
p1 = round((count_esfera/count_qtd) * 100, 2)
p2 = round((count_limpeza / count_qtd) * 100, 2)
p3 = round ((count_conector / count_qtd) * 100, 2)
p4 = round ((count_inutilizado / count_qtd) * 100, 2)


space = ' ' * 5
print(f'Situacao {space}       Quantidade {space} Percentual')
print(f'1 - Esfera {space}       {count_esfera} {space}         {p1}%')
print(f'2 - Limpeza {space}      {count_limpeza} {space}         {p2}%')
print(f'3 - Conector {space}     {count_conector} {space}         {p3}%')
print(f'4 - Inutilizado {space}  {count_inutilizado} {space}         {p4}%')



# Saida de Dados

# Soma dos defeitos
# Ordernadas
# Quantidade
# Percentual





