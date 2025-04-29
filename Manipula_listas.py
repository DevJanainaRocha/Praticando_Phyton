cidades = ['Rio de Janeiro', 'Brasília', 'Formosa']
#               0               1           2
print('Imprimindo todas as cidades:')
print(cidades, '\n')

print ('Imprimindo apenas o index desejado:')
print(cidades[2])
print(cidades[-2],'\n') #O index negativo conta de trás para frente

print('Alterando o valor do index 1:')
cidades[1] = 'Sobradinho'
print (cidades[1], '\n')

print ('Inserindo mais uma cidade no fim da lista:')
cidades.append('Maragogi') #O append insere item no final da lista
print(cidades, '\n')

print('removendo um item da lista:')
cidades.remove('Rio de Janeiro')
print(cidades,'\n')

print('Colocando as cidades em ordem alfabética:')
cidades.sort() # O sort põe os item em ordem alfabética
print(cidades)


