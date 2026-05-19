from random import randint

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
df_vendas.shape

# exibe as 5 primeiras linhas do DataFrame
df_vendas.head()

# exibe as 5 ultimas linhas do DataFrame
df_vendas.tail()

# exibe informações gerais sobre o DataFrame
df_vendas.info()

# resumo estatístico
df_vendas.describe()

# tipos de dados
df_vendas.dtypes