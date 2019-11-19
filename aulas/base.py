import pandas as pd
dt = pd.read_csv('../arquivos/salarios.csv')
#print(dt.head())
print(dt.iloc[1,1])
