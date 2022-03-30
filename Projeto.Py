import pandas as pd

tabela_vendas = pd.read_excel(r'C:\Users\flavi\OneDrive\Documentos\GitHub\Pandas\Vendas.xlsx')

faturamento = tabela_vendas['Valor Final'].sum()
quantidade = tabela_vendas['Quantidade'].sum()

print(f'O faturamento foi de R${faturamento:,.2f}')
print(f'Foram vendidos {quantidade} produtos')