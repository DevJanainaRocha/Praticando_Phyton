'''Criar um retângulo 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@'''

linha = 6
coluna = 6
simbolo = 'Janaina'

for l in range (linha):
    for c in range (coluna):
        print(f'{simbolo}', end='')
    print()#faz com que pule para a proxima linha a cada for impresso
