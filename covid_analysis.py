import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar dados
df = pd.read_csv('covid_data.csv')

# Limpeza de dados
df = df.dropna()
df['data'] = pd.to_datetime(df['data'])

# Análise temporal
df_daily_cases = df.groupby('data')['new_cases'].sum()
plt.figure(figsize=(10, 5))
plt.plot(df_daily_cases.index, df_daily_cases.values, label='Novos Casos')
plt.xlabel('Data')
plt.ylabel('Número de Casos')
plt.title('Novos casos de COVID-19')
plt.legend()
plt.show()

# Análise por região
df_country_cases = df.groupby('location')['total_cases'].max()
df_country_cases.sort_values(ascending=False).head(10).plot(kind='bar')
plt.xlabel('País')
plt.ylabel('Total de Casos')
plt.title('Total COVID-19 Cases by Country')
plt.show()

# Análise de mortalidade
df['mortality_rate'] = df['total_deaths'] / df['total_cases']
plt.scatter(df['total_cases'], df['mortality_rate'])
plt.xlabel('Total de Casos')
plt.ylabel('Taxa de Mortalidade')
plt.title('Taxa de Mortalidade vs Total de Casos')
plt.show()

# Correlações
correlation = df[['total_cases', 'total_deaths', 'total_tests']].corr()
import seaborn as sns
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
