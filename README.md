# Análise de Dados COVID-19

Este projeto realiza uma análise detalhada dos dados da pandemia de COVID-19 utilizando **Pandas** e **Matplotlib**. O objetivo é explorar tendências, padrões e insights nos dados de casos, mortes e testes relacionados à COVID-19.

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Análises Realizadas](#análises-realizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O projeto visa:

- Analisar dados temporais de casos e mortes por COVID-19.
- Explorar a distribuição dos casos por países.
- Investigar a correlação entre o número de casos, mortes e testes realizados.
- Visualizar as tendências e padrões através de gráficos.

Os dados são obtidos de fontes públicas, como [Our World in Data](https://ourworldindata.org/coronavirus-source-data) e [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).

## Instalação

### Pré-requisitos

Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado.

### Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Instalar Dependências

Instale as dependências necessárias com `pip`:

```bash
pip install -r requirements.txt
```

### Dependências

- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib**: Para criação de gráficos.

### Exemplo do `requirements.txt`

```
pandas
matplotlib
seaborn
```

## Uso

### Executar o Script de Análise

Para executar a análise, execute o script principal `covid_analysis.py`:

```bash
python covid_analysis.py
```

### Estrutura do Projeto

```
/
│
├── data/
│   └── covid_data.csv  # Dados CSV baixados
│
├── figures/
│   └── *.png  # Gráficos gerados
│
├── covid_analysis.py  # Script principal para análise
├── README.md  # Documentação do projeto
└── requirements.txt  # Dependências do projeto
```

## Análises Realizadas

### 1. **Análise Temporal**

Analisamos os casos diários ao longo do tempo para visualizar a evolução da pandemia.

![Daily New Cases](figures/daily_new_cases.png)

### 2. **Distribuição por País**

Visualizamos os casos acumulados por país para entender a distribuição global.

![Total Cases by Country](figures/total_cases_by_country.png)

### 3. **Taxa de Mortalidade**

Investigamos a relação entre o número total de casos e a taxa de mortalidade.

![Mortality Rate vs Total Cases](figures/mortality_rate_vs_total_cases.png)

### 4. **Correlação entre Variáveis**

Exploramos a correlação entre o número de casos, mortes e testes realizados.

![Correlation Matrix](figures/correlation_matrix.png)

## Contribuição

Contribuições são bem-vindas! Por favor, siga os passos abaixo para contribuir:

1. Fork este repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça as suas alterações.
4. Faça o commit (`git commit -m 'Adiciona nova funcionalidade'`).
5. Envie para a branch (`git push origin feature/nova-funcionalidade`).
6. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

