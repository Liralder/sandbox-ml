# Importanto as bibliotecas necessarias para rodar o modelo.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import xlrd

##################################################################################################################
# Carregando os dados do site Better Life Index.
oecd_bli = pd.read_csv(
    'src/betterlifeindex.csv', 
    thousands=',',
    delimiter=','
)

# Criação de filtros para remoção de duplicidades na base.
oecd_bli = oecd_bli.loc[(oecd_bli['Unit Code']=='PC') & (oecd_bli['INDICATOR']=='HO_BASE')]

# Selecionando as colunas que serão mais importantes da Better Life Index.
oecd_bli = oecd_bli[['Country', 'LOCATION', 'Value']]

# Renomeando as colunas da Better Life Index.
oecd_bli = oecd_bli.rename(columns={'Country': 'País', 'LOCATION': 'Sigla', 'Value': 'Satisfação de Vida'})

# Apresentando os dados da Better Life Index.
oecd_bli.head(3)

##################################################################################################################
# Carregando os dados de estatísticas sobre o PIB per capita do site FMI
per_capita = pd.read_csv(
    'src/percapita.csv', 
    thousands=',',
    delimiter=','
)

# Selecionando as colunas que serão mais importantes da Better Life Index.
per_capita = per_capita[['Country Name', 'Country Code', '2021']]

# Renomeando as colunas da Better Life Index.
per_capita = per_capita.rename(columns={'Country Name': 'País', 'Country Code': 'Sigla', '2021': 'PIB'})

# Apresentando os dados da Better Life Index.
per_capita.head(3)

##################################################################################################################
# Preparando os dados para visualização.
country_stats = pd.merge(
    oecd_bli, 
    per_capita, 
    how='left', 
    on=['País', 'Sigla']
)

print(country_stats)
##################################################################################################################
# Visualização de dados para observação da distribuição.
X = np.c_[country_stats['PIB']]
y = np.c_[country_stats['Satisfação de Vida']]

country_stats.plot(
    kind='scatter', 
    x='PIB', 
    y='Satisfação de Vida'
)

plt.show()