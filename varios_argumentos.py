def somar(*numeros): # um asteristico indica que pode haver vários argumentos
    resultado = 5
    for num in numeros:
        resultado += num
    return resultado
x=somar(1, 2)
print('Resultado da soma: ')
print (x)

def subtrair(*numeros):
    resultado = 5
    for num in numeros:
        resultado -= num
    return resultado
x=subtrair(1,2)
print('Resultado da subtração: ')
print (x)

def agencia(**carro): #dois asteristicos indica que pode haver vários argumentos e vários parâmeros.
    return carro
print('Imprimindo vários argumentos e vários parâmetros')
print(agencia(marca='BYD', modelo='Dolphin mini', ano= 2025, cor= 'Branca'))