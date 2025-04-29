numeros = [1,2,3,4,5]
letras = ['a', 'b', 'c',]
print('Imprimindo a lista de letras:')
print (letras, '\n')

itens = [[1,2,3,4,5],['a','b','c','d','e']]
print('Imprimindo o index da primeira lista:')
print(itens[0],'\n')

print('Imprimindo o index da segunda lista:')
print(itens[1], '\n')

print('Imprimindo o item de uma determinada posição no index:')
print(itens[1][0])
print(itens[0][2], '\n')

print('Escolhendo o item que se deseja imprimir:')
item1, item2, *outros, item5 = numeros # *outros indica os itens da lista que não foram mencionados 
print(outros)
print(item5, '\n')


print('Inserindo uma lista dentro de outra: \n')
numeros.extend(letras) #o extend acrescenta uma lista dentro de outra
print(numeros)