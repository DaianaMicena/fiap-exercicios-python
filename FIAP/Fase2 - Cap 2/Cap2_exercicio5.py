#5 votos
#escolhido e mais votado
#playstation
#nintendo
#x box

#Revisar

mais_votado = 0
escolhido = " "

p1 = 'nintendo'    #str(input("Escolha o video game? "))
p2 = 'nintendo'       #str(input("Escolha o video game? "))
p3 = 'nintendo'   #str(input("Escolha o video game? "))
p4 = 'xbox'       # str(input("Escolha o video game? "))
p5 = 'nintendo'   #str(input("Escolha o video game? "))

if p1 == 'nintendo':
    mais_votado = 1
    escolhido = 'nintendo'
elif p1 == 'xbox':
    mais_votado = 1
    escolhido = 'xbox'
elif p1 == 'playstation':
    mais_votado = 1
    escolhido = 'playstation'

if p2 == 'nintendo':
    mais_votado = 1
    escolhido = 'nintendo'
elif p2 == 'xbox':
    mais_votado = 1
    escolhido = 'xbox'
elif p2 == 'playstation':
    mais_votado = 1
    escolhido = 'playstation'

print(f"O console mais votado foi {escolhido} com {mais_votado} votos")




