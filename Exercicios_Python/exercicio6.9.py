#entrada
indice = (float(input("Informe o indice de poluicao")))

#processamento
if indice >= 0.3 and indice < 0.4:
    print("Empresas do grupo 1 deverao suspender as atividades")
elif indice > 0.4 and indice < 0.5:
    print("Empresas do grupo 1 e 2 deverao suspender as atividades")
elif indice >= 0.5:
    print("Todas as empresas deverao ser suspensas")
else:
    print("Niveis aceitaveis")
