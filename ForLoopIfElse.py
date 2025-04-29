compra_confirmada = True
dados_da_compra = 'Compra no valor de R$ 50,00 e entrega confirmada para 25.04.2025'

for enviar in  range(3):
    if compra_confirmada:
        print(dados_da_compra)
        print('Detalhes enviados ara o seu e-mail') 
        '''O break retorna para o loop antes de imprimir até 
        que seja executada a quantidade de vezes estabelecida no range.
        Sem o break no código, o resultado do print apareceria 3x '''
        break 
    else:
        print('Compra não confirmada')
