# O set evita itens duplicados
#O set converte a lista para set

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 30, 60, 70]

nun1 = set(lista1) 
nun2 = set(lista2)

print ('Imprimindo sem repetir os duplicados:')
print (nun1 | nun2, '\n') # O | indica union, que imprime todos os valores sem repetir

print ('Imprimindo valores da primeira que não têm na segunda:')
print (nun1 - nun2, '\n') # O - indica difference, que só imprime os valores da 1º que não tem na 2º lista

print ('Imprimindo valores de ambas as listas, mas que não se reptem:')
print (nun1 ^ nun2, '\n') # O ^ indica symetric difference, que imprime valores únicos de ambas as listas

print ('Imprimindo apenas valores que possuem em ambas as listas:')
print (nun1 & nun2) # O & indica and que imprime os valores que se repetm em ambas as listas
