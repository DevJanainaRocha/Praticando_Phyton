from datetime import datetime #para importar a data atual
class Funcionarios:
    def __init__ (self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome= sobrenome
        self.nascimento = nascimento

    def dados_funcionario (self):

        return self.nome +' '+self.sobrenome + ' / Ano de nascimento: ' + self.nascimento  
    
    def idade_funcionario (self): 
        ano_atual = datetime.now().year # para importar o ano atual dentro do date time
        self.idade = int(ano_atual - self.nascimento)
        return self.idade 

funcionario1 = Funcionarios('Janaina', 'Rocha', '1982')
funcionario2= Funcionarios('Rogerio', 'Moraes', 1981)

print('Imprimindo os dados do funcionário 1: ')
print (Funcionarios.dados_funcionario(funcionario1),'\n')

#print (Funcionarios.dados_funcionario(funcionario2), '\n')
print('Imprimindo a idade do funcionário 2: ')
print(Funcionarios.idade_funcionario(funcionario2), 'anos de idade')
