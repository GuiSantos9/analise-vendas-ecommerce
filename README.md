# 📊 Análise de Vendas — E-commerce

Mini-projeto de análise exploratória de dados de vendas fictícias, desenvolvido durante a formação da **Data Science Academy**. O projeto abrange desde a geração sintética dos dados até a visualização de insights por meio de gráficos.

---

## 🎯 Objetivo

Praticar os fundamentos de análise de dados com Python, passando pelas etapas de geração de dados, limpeza, pré-processamento, engenharia de atributos e visualização — construindo uma pipeline completa do zero.

---

## 🗂️ Estrutura do Projeto

```
análise-vendas-ecommerce/
│
├── analise_vendas.py       # Script principal com toda a pipeline
└── README.md
```

---

## ⚙️ Pipeline

```
Geração de Dados  →  Limpeza & Pré-processamento  →  Engenharia de Atributos  →  Análise  →  Visualização
```

### 1. Geração de Dados Sintéticos
- Dataset com **500 registros** de vendas gerados aleatoriamente
- **8 produtos** em 3 categorias: Estofados, Eletrodomésticos e Móveis
- **7 cidades** distribuídas entre 7 estados brasileiros
- Atributos gerados: ID do pedido, data, produto, categoria, preço unitário, quantidade, cliente, cidade e estado

### 2. Limpeza & Pré-processamento
- Conversão da coluna `Data_Pedido` para o tipo `datetime`
- Criação da coluna `Faturamento` (`Preco_Unitario × Quantidade`)
- Criação da coluna `Status_Entrega` com base no estado (`Rápida` para SP, RJ e MG)

### 3. Análises Realizadas

| # | Análise | Tipo de Gráfico |
|---|---------|-----------------|
| 1 | Top 10 produtos mais vendidos | Barras horizontais |
| 2 | Evolução do faturamento mensal | Linha |
| 3 | Faturamento total por categoria | Barras verticais |
| 4 | Faturamento por estado | Barras verticais |

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca | Uso |
|------------|-----|
| `pandas` | Manipulação e análise de dados |
| `numpy` | Geração de valores aleatórios e cálculos numéricos |
| `matplotlib` | Criação dos gráficos |
| `seaborn` | Estilização dos gráficos |

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.8+

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/analise-vendas-ecommerce.git
cd analise-vendas-ecommerce
```

2. Instale as dependências:
```bash
pip install pandas numpy matplotlib seaborn
```

3. Execute o script:
```bash
python analise_vendas.py
```

---

## 💡 Aprendizados

Mesmo sendo um projeto introdutório, foi possível perceber a importância da análise de dados como base para o aprendizado de máquina. Dados bem estruturados, explorados e visualizados são o alicerce de qualquer modelo de IA — entender essa etapa é essencial para quem deseja atuar em Engenharia de IA.

---

## 📌 Status

✅ Concluído — Parte da trilha de formação da **Data Science Academy**

---

