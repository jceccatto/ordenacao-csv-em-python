import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 999)
dados = pd.read_csv('dados.csv')
#print(dados.head())
#print(dados.columns)
dados.info()
print(dados.head())
dados['Qual setor/gabinete você está lotado/a?1'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]1'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?2'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]2'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?3'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]3'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?4'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]4'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?5'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]5'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?6'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]6'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?7'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]7'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?8'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]8'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?9'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]9'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?10'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]10'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?11'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]11'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?12'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]12'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a?13'].fillna('',inplace=True)
dados['Qual setor/gabinete você está lotado/a? [Outros]13'].fillna('',inplace=True)
dados['Setor'] = dados['Qual setor/gabinete você está lotado/a?1'] + dados['Qual setor/gabinete você está lotado/a? [Outros]1'] + dados['Qual setor/gabinete você está lotado/a?2'] + dados['Qual setor/gabinete você está lotado/a? [Outros]2'] + dados['Qual setor/gabinete você está lotado/a?3'] + dados['Qual setor/gabinete você está lotado/a? [Outros]3'] + dados['Qual setor/gabinete você está lotado/a?4'] + dados['Qual setor/gabinete você está lotado/a? [Outros]4'] + dados['Qual setor/gabinete você está lotado/a?5'] + dados['Qual setor/gabinete você está lotado/a? [Outros]5'] + dados['Qual setor/gabinete você está lotado/a?6'] + dados['Qual setor/gabinete você está lotado/a? [Outros]6'] + dados['Qual setor/gabinete você está lotado/a?7'] + dados['Qual setor/gabinete você está lotado/a? [Outros]7'] + dados['Qual setor/gabinete você está lotado/a?8'] + dados['Qual setor/gabinete você está lotado/a? [Outros]8'] + dados['Qual setor/gabinete você está lotado/a?9'] + dados['Qual setor/gabinete você está lotado/a? [Outros]9'] + dados['Qual setor/gabinete você está lotado/a?10'] + dados['Qual setor/gabinete você está lotado/a? [Outros]10'] + dados['Qual setor/gabinete você está lotado/a?11'] + dados['Qual setor/gabinete você está lotado/a? [Outros]11'] + dados['Qual setor/gabinete você está lotado/a?12'] + dados['Qual setor/gabinete você está lotado/a? [Outros]12'] +dados['Qual setor/gabinete você está lotado/a?13'] + dados['Qual setor/gabinete você está lotado/a? [Outros]13']
dados.drop(['Qual setor/gabinete você está lotado/a?1', 'Qual setor/gabinete você está lotado/a? [Outros]1', 'Qual setor/gabinete você está lotado/a?2', 'Qual setor/gabinete você está lotado/a? [Outros]2', 'Qual setor/gabinete você está lotado/a?3','Qual setor/gabinete você está lotado/a? [Outros]3','Qual setor/gabinete você está lotado/a?4','Qual setor/gabinete você está lotado/a? [Outros]4','Qual setor/gabinete você está lotado/a?5','Qual setor/gabinete você está lotado/a? [Outros]5','Qual setor/gabinete você está lotado/a?6','Qual setor/gabinete você está lotado/a? [Outros]6','Qual setor/gabinete você está lotado/a?7','Qual setor/gabinete você está lotado/a? [Outros]7','Qual setor/gabinete você está lotado/a?8','Qual setor/gabinete você está lotado/a? [Outros]8','Qual setor/gabinete você está lotado/a?9','Qual setor/gabinete você está lotado/a? [Outros]9','Qual setor/gabinete você está lotado/a?10','Qual setor/gabinete você está lotado/a? [Outros]10','Qual setor/gabinete você está lotado/a?11','Qual setor/gabinete você está lotado/a? [Outros]11','Qual setor/gabinete você está lotado/a?12','Qual setor/gabinete você está lotado/a? [Outros]12','Qual setor/gabinete você está lotado/a?13','Qual setor/gabinete você está lotado/a? [Outros]13'],axis=1,inplace=True)
dados2 = dados.sort_values(by=['Qual a unidade em que você está lotado/a?','Setor','Nome:'],ascending=[True, True, True])
print(dados2['Setor'])
dados2.to_csv('dados2.csv', index=False)

