cores = ['verde', 'vermelho', 'azul', 'amarelo']
cor_cliente = input('Digite a cor desejada: ')
#O lower considera tudo que o usuário digitar como letra minúscula
#O lower esta sendo utilizado como prevenção, pois as cores estão em minúsculo.
if cor_cliente.lower() in cores: 
    print ('Temos esta cor em estoque')
else:
    print ('Não temos mais esta cor')