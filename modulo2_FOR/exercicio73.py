times = ('Corinthians','Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atletico - PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atletico - GO')

print('='* 100)
print(f'Os primeiros 5 times sao: {times[:5]}')
print('='* 100)
print(f'Os ultimos colocados foram: {times[-4:]}')
print('='* 100)
print(f'Os times ordem alfabetica sao: {sorted(times)}')
print('='* 100)
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posicao.')