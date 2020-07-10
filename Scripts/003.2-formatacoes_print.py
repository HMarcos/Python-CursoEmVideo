print('-----------------------')
print('Formatações com Strings')
print('-----------------------')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:+^20}!'.format(nome))

""" 
Operações
X - valor inteiro que indica a quantidade de caracteres
:X - Escreve o atributo com X caracteres;
:<X - Alinhamento à Esquerda;
:>X - Alinhamento à  Direta;
:^X - Alinhamento à  Centralizado;
:(Símbolo)(Alinhamento)X  - Alinhamento com preenchimento do símbolo 
"""

print('-----------------------')
print('Formatações com Números')
print('-----------------------')

n1 = int(input('Informe um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print ('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s,m,d), end = ' >>> ')
print ('Divisão inteira: {}  \nPotência: {}'.format(di,e))

# Para Floats: {:.Df} - D indica a quantidade de casas decimais a ser exibida
# end = " " - Altera o final do print trocando a quebra de linha pelo conteúdo que estão entre aspas
# \n - insere uma quebra de linha