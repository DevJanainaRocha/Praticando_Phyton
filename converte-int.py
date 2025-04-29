'''O input sempre entende que se gtrata de str, portanto
sempre que necessário deve-se coverter pata int'''

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))

print(f'Meu nome é {nome} e tenho {idade} anos')

valor=int(input('Digite o valor do produto: '))
resultado = valor*1.10
print(f'O valor de {valor} mais os 10% é igual a: {resultado}')