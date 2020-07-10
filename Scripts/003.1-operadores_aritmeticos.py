print('--------------------------')
print('Operações com Aritméticas')
print('-------------------------')

e1 = 5+3*2 # Precedência: Multiplicação --> Adição
print('5+3*2 = {}'.format(e1))

e2 = 3*5+4**2 # Precedência: Potenciação -- >Multiplicação --> Adição
print('3*5+4**2 = {}'.format(e2))

e3 = 3*(5+4)**2 # Precedência: Parênteses(Soma) --> Potenciação -- >Multiplicação 
print('3*(5+4)**2 = {}'.format(e3))

e4 = pow(8,4) # Potenciação
print('pow(8,4) = {}'.format(e4))

e5 = 16**(1/2) # Radiciação
print('16**(1/2) = {}'.format(e5))

""" Com Strings """
print('----------------------')
print('Operações com Strings')
print('----------------------')

e6 = 'Marcos' + ' Henrique' # Concatenação
print('Concatenação: Marcos + Henrique = {}'.format(e6))

e7 = '='*20 # Repete a strig X vezes
print('Repetição da string: =*20  = {}'.format(e7)) 

