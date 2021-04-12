num = 0

while True:
    print('=================================')
    num = int(input('Digite um número: '))

    if num <= 0:
        break

    for c in range (1,11):

        print(f'{num} x {c} = {num*c} ')

  #  print(f' {num} x 1 = {num*1} \n {num} x 2 = {num*2} \n {num} x 3 = {num*3} \n {num} x 4 = {num*4} \n {num} x 5 = {num*5}')
  # print(f' {num} x 6 = {num*6} \n {num} x 7 = {num*7} \n {num} x 8 = {num*8} \n {num} x 9 = {num*9} \n {num} x 10= {num*10}')

print('Fim!!!')




