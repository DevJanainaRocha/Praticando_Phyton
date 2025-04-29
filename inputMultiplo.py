dados = input('Digite o seu nme e sua idade: ').split() # Janaina  42 (split separa os espaços)
nome = dados[0]
idade = dados[1]

'''upper() ao lado da variável str 
   deixa tudo em letra maiúscula'''

print(f'Meu nome e {nome.upper()} e tenho {idade} anos')