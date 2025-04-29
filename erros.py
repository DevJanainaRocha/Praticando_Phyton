#try /  except

'''Os erros são exelentes para testes. ele não realiza o stop no programa,
ou seja, permite que o programa continue rodando.
No exemplo abaixo o index não exixte, poi ele vao apenas do  ao 3'''

try:
    letras = ['a', 'b', 'c']
    print (letras [3])
except IndexError:
    print ('Imprimindo erro de index:')
    print ('Index não existe \n')

try:
    valor = int(input('Digite um número: '))
    print('Imprimindo erro de valor no input: ')
    print (valor)
except ValueError: #o excep deve ser sempre dentro do tipo de erro
    print('O valor digitado não é um número. Por favor digitar um valor válido \n')

print('Mais código') #com o try / except os demais códigos continuam rodando