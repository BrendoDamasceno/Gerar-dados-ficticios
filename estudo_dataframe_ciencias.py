#Estudo Datagame
import pandas as pd

#Lista: uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nome = ['Ana', 'Marcos', 'Carlos']
print('Lista de nomes: \n', lista_nome)
print('Primeiro Elemento na lista: \n ', lista_nome[0])

#Dicionario: Estrutura composta de pares chave-valor
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 20,
    'cidade': 'São paulo'
}

print('Dicionário de uma pessoa: \n', dicionario_pessoa)
print('Atributo do Dicionario: \n ', dicionario_pessoa.get('nome'))

dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'São paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'São jose dos campos'},
    {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio de janeiro'},
]

#DataFrame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n', df)

#Selecionar coluna
print(df['nome'])

#Selecionar várias colunas
print(df[['nome', 'idade']])


#Selecionar linhaas pelo indice
print('Primeira linha \n', df.iloc[0])

#Adicionar uma nova coluna
df['salario'] = [4100, 3600, 5200]

#Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'Teresina',
    'salario': 4800
}

print('DataFrame Atual \n', df)


#Removendo uma coluna
df.drop('salario', axis=1, inplace=True)


#Filtrando pessoa com mais de 29 ano
filtro_idade = df[df['idade'] >= 30]
print(('Filtro \n', filtro_idade))


#Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)


#Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print(('\n leiture do CSV \n', df_lido))