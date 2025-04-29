#exelentes para loops dependentes de uma condição
# criando promoção 

valor = 100
dia = 0
while valor > 20:
    dia += 1
    print (f'No dia {dia} o valor será R$ {valor}')
    '''A condição acima sozinha, cria um lopping infinito,
    mas após fornecer desconto de 5 reais no valor(conforme abaixo) o looping 
    rodará até que o valor permaneça maio que 20'''
    
    valor -= 5