'''Em python as array precisam ser importadas.
A arrays são como matrizes '''

from array import array

letras = ['a', 'b', 'c', 'd']
inteiros = [1, 2, 3, 4,]
flutuantes = [1.2, 2.5, 1.4, 3.2]
print(letras)
print(inteiros)
print(flutuantes)
print()
# conertendo as listas acima em array
# o 'u' é um type code que indica que se trata de uma array de caracteres/ str
# o 'i' é um type code que indica se tratar de array de inteiros
# o 'f' é um type code que indica se tratar de array de numeros float

letras = array('u', ['a', 'b', 'c', 'd'] ) 
inteiros = array('i', [1, 2, 3, 4,] ) 
flutuantes = array('f', [1.2, 2.5, 1.4, 3.2])

print ('Imprimindo arrays de letras:')
print (letras, '\n')

print ('Imprimindo arrays de inteiros:')
print (inteiros, '\n')

print ('Imprimindo arrays de flutuantes:')
print (flutuantes)