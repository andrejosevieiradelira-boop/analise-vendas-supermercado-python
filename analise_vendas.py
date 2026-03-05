# No iremos python abrir planilha percorrer a planilha.
import pandas as pd
import matplotlib.pyplot as plt
# ler o arquivo excel
df = pd.read_excel("vendas_supermercado_sp.xlsx") 
print(df)

# Pegar na planilha a coluna cidade, coluna Faturamento_Mes1, coluna Faturamento_Mes2, coluna Faturamento_Mes3
# e somar o total do faturamento de cada loja e por mes.

for index, row in df.iterrows():             # iterrows() é um método do pandas que permite iterar sobre as linhas de um DataFrame. Ele retorna um gerador que produz tuplas contendo o índice da linha e os dados da linha como uma série do pandas.
    cidade = row['Cidade']                      # Acessa o valor da coluna 'Cidade' para a linha atual e armazena na variável cidade.
    faturamento_mes1 = row['Faturamento_Mes1']      # Acessa o valor da coluna 'Faturamento_Mes1' para a linha atual e armazena na variável faturamento_mes1.
    faturamento_mes2 = row['Faturamento_Mes2']      
    faturamento_mes3 = row['Faturamento_Mes3']
    
    total_faturamento = faturamento_mes1 + faturamento_mes2 + faturamento_mes3    # Calcula o total do faturamento somando os valores dos três meses e armazena na variável total_faturamento.
    
    print(f"Cidade: {cidade}, Total Faturamento: {total_faturamento}")

# soma o total do faturamento de todas as lojas de as e mes junto.
soma_total_faturamento = df['Faturamento_Mes1'].sum() + df['Faturamento_Mes2'].sum() + df['Faturamento_Mes3'].sum()    # Calcula a soma total do faturamento para os três meses somando as somas de cada coluna e armazena na variável soma_total_faturamento.
print(f"Soma Total do Faturamento: {soma_total_faturamento}")

# ver media por loja, por mes.
def calcular_media_faturamento(df):
    media_mes1 = df['Faturamento_Mes1'].mean()    # Calcula a média do faturamento para o mês 1 usando o método mean() do pandas e armazena na variável media_mes1.
    media_mes2 = df['Faturamento_Mes2'].mean()    # Calcula a média do faturamento para o mês 2 e armazena na variável media_mes2.
    media_mes3 = df['Faturamento_Mes3'].mean()    # Calcula a média do faturamento para o mês 3 e armazena na variável media_mes3.
    
    print(f"Média Faturamento Mês 1: {media_mes1}")
    print(f"Média Faturamento Mês 2: {media_mes2}")
    print(f"Média Faturamento Mês 3: {media_mes3}")

media_mes_faturamento = calcular_media_faturamento(df)      # Chama a função calcular_media_faturamento passando o DataFrame df e armazena o resultado na variável media_mes_faturamento. No entanto, a função calcular_media_faturamento não retorna nenhum valor, então media_mes_faturamento será None.
print(f"Média Faturamento por Mês:\n{media_mes_faturamento}")

# Agora media por loja

def calcular_media_faturamento_loja(df):            # Define a função calcular_media_faturamento_loja que recebe um DataFrame df como argumento.
    media_faturamento_loja = df.groupby('Cidade')[['Faturamento_Mes1', 'Faturamento_Mes2', 'Faturamento_Mes3']].mean()    # Agrupa o DataFrame por cidade usando groupby() e calcula a média do faturamento para cada loja e mês usando mean(), armazenando o resultado na variável media_faturamento_loja.
    return media_faturamento_loja

media_faturamento_loja = calcular_media_faturamento_loja(df)    # Chama a função calcular_media_faturamento_loja passando o DataFrame df e armazena o resultado na variável media_faturamento_loja.
print(f"Média Faturamento por Loja e Mês:\n{media_faturamento_loja}")

# qual foi o maior faturamento por loja e mes
maior_faturamento_mes = df.groupby('Cidade')[['Faturamento_Mes1', 'Faturamento_Mes2', 'Faturamento_Mes3']].max()    # Agrupa o DataFrame por cidade e calcula o maior faturamento para cada loja e mês usando max(), armazenando o resultado na variável maior_faturamento_loja_mes.
print(f"Maior Faturamento por Loja e Mês:\n{maior_faturamento_mes  }")


# qual foi o menor faturamento por loja e por mes
menor_faturamento_mes = df.groupby('Cidade')[['Faturamento_Mes1', 'Faturamento_Mes2', 'Faturamento_Mes3']].min()    # Agrupa o DataFrame por cidade e calcula o menor faturamento para cada loja e mês usando min(), armazenando o resultado na variável menor_faturamento_loja_mes.
print(f"Menor Faturamento por Loja e Mês:\n{menor_faturamento_mes  }")

# calcular margem de lucro por mes
margem_lucro_mes1 = df['Lucro_Mes1'] / df["Faturamento_Mes1"]    # Calcula a margem de lucro para o mês 1 multiplicando o faturamento do mês 1 por 0.2 (20%) e armazena na variável margem_lucro_mes1.
margem_lucro_mes2 = df['Lucro_Mes2'] / df["Faturamento_Mes2"]
margem_lucro_mes3 = df['Lucro_Mes3'] / df["Faturamento_Mes3"]


# editar em 2 casas decimais e porcentagem
margem_lucro_mes1 = margem_lucro_mes1.apply(lambda x: f"{x:.2%}")    # Aplica uma função lambda para formatar os valores da margem de lucro do mês 1 como porcentagem com duas casas decimais.
margem_lucro_mes2 = margem_lucro_mes2.apply(lambda x: f"{x:.2%}")    # Aplica a mesma formatação para a margem de lucro do mês 2.
margem_lucro_mes3 = margem_lucro_mes3.apply(lambda x: f"{x:.2%}")    # Aplica a mesma formatação para a margem de lucro do mês 3.
print(f"Margem de Lucro Mês 1:\n{margem_lucro_mes1}")
print(f"Margem de Lucro Mês 2:\n{margem_lucro_mes2}")
print(f"Margem de Lucro Mês 3:\n{margem_lucro_mes3}")


# Fazer um grafico com essa infomações


# calcular total por loja
df["Total_Faturamento"] = df["Faturamento_Mes1"] + df["Faturamento_Mes2"] + df["Faturamento_Mes3"]

# criar gráfico
plt.figure()
plt.bar(df["Cidade"], df["Total_Faturamento"])

plt.title("Faturamento Total por Loja")
plt.xlabel("Cidade")
plt.ylabel("Faturamento")

plt.xticks(rotation=45)

plt.show()



faturamento_mes = [
    df["Faturamento_Mes1"].sum(),
    df["Faturamento_Mes2"].sum(),
    df["Faturamento_Mes3"].sum()
]

meses = ["Mês 1", "Mês 2", "Mês 3"]

plt.figure()
plt.bar(meses, faturamento_mes)

plt.title("Faturamento Total por Mês")
plt.xlabel("Meses")
plt.ylabel("Faturamento")

plt.show()
