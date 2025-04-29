temperatura = int(input('Digite um valor que indique a temperatura da sua cidade neste momento: '))
if temperatura < 10:
    print('Está frio')
elif temperatura < 20 :
    print('Está freco')
else:
    print('Está Calor')