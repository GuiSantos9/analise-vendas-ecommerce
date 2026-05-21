from random import randint

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import random
from datetime import datetime,timedelta

def dados_ficticios(numero_de_registros = 600):

    """
    Gera um DataFrame do Pandas com dados de vendas ficticios
    """

    print(f"\nIniciando a geração de {numero_de_registros} registros vendas...")

    produtos = {
        'Sofá Retratil': {'categoria':'Estofados', 'preco':7000.00},
        'Poltrona Opala': {'categoria': 'Estofados', 'preco': 360.00},
        'Puff': {'categoria': 'Estofados', 'preco': 70.00},
        'Geladeira': {'categoria': 'Eletro Domesticos', 'preco': 9000.00},
        'Cama': {'categoria': 'Móveis', 'preco': 3000.00},
        'Cadeira Pétala': {'categoria': 'Estofados', 'preco': 7000.00},
        'Sofá Fixo': {'categoria': 'Estofados', 'preco': 2000.00},
        'Almofada': {'categoria': 'Estofados', 'preco': 50.00},
    }

    # crio uma lista com apenas o nome dos produtos
    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo':'SP', 'Rio de Janeiro':'RJ', 'Curitiba':'PR',
        'Belo Horizonte': 'MG', 'Porto Alegre': 'RS', 'Salvador': 'BA', 'Fortaleza': 'CE'
    }

    # crio uma lista com apenas o nome das cidades
    lista_cidades = list(cidades_estados.keys())

    # lista que armazena os registros de vendas
    dados_vendas = []

    # data inicial dos pedidos
    data_inicial = datetime(2026,5,16)

    # loop para gerar o registro de vendas
    for i in range(numero_de_registros):

        produto_nome = random.choice(lista_produtos)
        cidades = random.choice(lista_cidades)
        quantidade = np.random.randint(1,8)

        # calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # se o produto for Poltrona Opala ou Puff, se aplica um desconto de 10%
        if produto_nome in ["Poltrona Opala", "Puff"]:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else :
            preco_unitario = produtos[produto_nome]['preco']

        # adiciona um registro de vendas
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria':produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade' : quantidade,
            'ID_Cliente': np.random.randint(100,150),
            'Cidade': cidades,
            'Estado':cidades_estados[cidades]
        })

    print("Geração de Dados concluída!\n")
    return pd.DataFrame(dados_vendas)

# gera os dados chamando a função da célula anterior
df_vendas = dados_ficticios(500)

# shape
print(df_vendas.shape)

# exibe as 5 primeiras linhas do DataFrame
print(df_vendas.head())

# exibe as 5 ultimas linhas do DataFrame
print(df_vendas.tail())

# exibe informações gerais sobre o DataFrame
df_vendas.info()

# resumo estatístico
print(df_vendas.describe())

# tipos de dados
print(df_vendas.dtypes)

#limpeza pré-processamento e engenharia de atributos
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in
                                                        ['SP', 'RG', 'MG'] else 'Normal' )

df_vendas.info()

print(df_vendas.head())

# Análise
# aqui eu agrupo os produtos por nome e ordeno para mostrar os 10 produtos mais vendidos
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

print(top_10_produtos)

# gráfico

# definir estilo de gráfico usando o sns
sns.set_style("whitegrid")

# criar a figura e os eixos
plt.figure(figsize= (12, 7))
# criar gráficos de barras horizontais pelo plot plt
top_10_produtos.sort_values(ascending=True).plot(kind='barh', color="skyblue")

# criar os títulos e labels
plt.title("Top 10 Produtos mais vendidos", fontsize = 16)
plt.xlabel("Quantidade Vendida", fontsize = 12)
plt.ylabel("Produtos", fontsize = 12)

# exibir o gráfico
plt.tight_layout()
plt.show()


# Faturamento Mensal
# criar uma coluna 'Mes' para facilitar o grupamento mensal
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')

# agrupo os mêses e somo(sum) seus faturamentos
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()

# converto o index para string para facilitar a plotagem
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

# Formato para duas casas decimais
# pega o que está em parêntes e vai aplicar no data frame
faturamento_mensal.map('R$ {:,.2f}'.format)

# criar a figura e os eixos
plt.figure(figsize= (12, 6))

#plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind = 'line', marker = 'o', color = 'green')

#título e labels
plt.title('Evolução do Faturamento Mensal', fontsize = 16)
plt.xlabel('Mês', fontsize = 12)
plt.ylabel('Faturamento {R$}', fontsize = 12)

# rotaciona os valores do eixo x em 45 graus para melhor visualização
# xticks são os labels de x porém colocamos uma inclinação
plt.xticks(rotation = 45)

# adiciona uma grade com estilo tracejado e linhas finas
plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)

# ajusta os elementos automaticamente para não ter sobreposição
plt.tight_layout()

#exibe o gráfico
plt.show()

# Análise de vendas por Estado
vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)

vendas_estado.map('R$ {:,.2f}'.format)

plt.figure(figsize= (12, 7))

vendas_estado.plot(kind = "bar", color = sns.color_palette("husl", 7))

plt.title('Análise de vendas por Estado', fontsize = 16)
plt.xlabel('Estado', fontsize = 12)
plt.ylabel('Faturamento {R$}', fontsize = 12)

plt.xticks(rotation = 0)

plt.tight_layout()

plt.show()

# Análise de Faturamento Total por Categoria

faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

faturamento_categoria.map('R$ {:,.2f}'.format)

# ordena os dados do gráfico para facilitar a leitura
faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

# cria a figura e os eixos (ax) com plt.subplots()
# isso nos dá mais controle sobre os elementos do gráfico
fig, ax = plt.subplots(figsize= (12, 7))

# cria uma função para formatar números
# ela recebe um valor 'y' e o transforma em uma string no formato 'R$ XX K'
def formatador_milhares(y, pos):
    return f'R$ {y/1000:,.0f}K'

# cria um objeto formatador
formatter = FuncFormatter(formatador_milhares)

# aplica o formatador ao eixo y
ax.yaxis.set_major_formatter(formatter)

# faturamento ordenado
faturamento_categoria.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(faturamento_ordenado)))

ax.set_title("Faturamento por Categoria", fontsize = 16)
ax.set_xlabel("Categoria", fontsize = 12)
ax.set_ylabel("Faturamento", fontsize = 12)

plt.xticks(rotation = 45, ha = "right")

plt.tight_layout()

plt.show()

