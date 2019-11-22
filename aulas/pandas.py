import pandas as pd
df = pd.read_csv('../arquivos/salarios.csv')
#print(dt.head())
# var = df['Name']
# var.to_csv('../arquivos/name.csv',header=0)
# print(df.loc[20,['Name', 'Department']]) # paramentro loc: numero da linha, nome da coluna
# var2 = df.loc[20, ['Name', 'Employee Annual Salary']]
# #parametros iloc: numero da linha, index da coluna
# print(df.iloc[20,2])
# var2.to_csv('valor_unico.csv', header=0)

df.to_csv('novo_salario.csv', header=0, sep=';')

