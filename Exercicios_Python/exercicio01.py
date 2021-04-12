#entradas
quantidade_minima = int(input("Informe a quantidade mínima:"))
quantidade_maxima = int(input("Informe a quantidade máxima:"))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saída
print("O estoque médio é {0}".format(estoque_medio))

