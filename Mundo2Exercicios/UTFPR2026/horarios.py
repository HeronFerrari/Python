import plotly.graph_objects as go
import pandas as pd

# 1. Preparar os dados (exemplo: horários da semana)
data = {
    'Horário': ['19:00 - 19:45', '19:45 - 20:30', '20:30 - 21:15', '21:30 - 22:15', '22:15 - 23:00'],
    'Segunda': ['', '', '', 'tcc1(7º)', 'tcc1(7º)'],
    'Terça': ['en14sw(4º)', 'en14sw(4º)', '', '',''],
    'Quarta': ['pc17sw(7º)', 'pc17sw(7º)', '', '',''],
    'Quinta': ['', '', '', '',''],
    'Sexta': ['pc17sw(7º)', 'pc17sw(7º)', '', '',''],
}

data2 = {
    'Horário': ['19:00 - 19:45', '19:45 - 20:30', '20:30 - 21:15', '21:30 - 22:15', '22:15 - 23:00'],
    'Segunda': ['', '', 'rc14sw(3º)', 'rc14sw(4º)', 'rc14sw(4º)'],
    'Terça': ['', '', '', '',''],
    'Quarta': ['', '', '', '',''],
    'Quinta': ['', '', '', '',''],
    'Sexta': ['', '', '', '',''],
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# 2. Criar a tabela com Plotly
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(df.columns),
        fill_color='darkblue',
        align='left',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[df.Horário, df.Segunda, df.Terça, df.Quarta, df.Quinta, df.Sexta],
        fill_color='lavender',
        align='left',
        font=dict(color='black', size=11),
        height=30 # Aumenta a altura das linhas
    )
)])

# 3. Configurar layout (título e tamanho)
fig.update_layout(
    title='Matérias que não fiz, estão fora do prazo 2 do 7º e 1 do 4º',
    width=800,
    height=400
)

fig2 = go.Figure(data=[go.Table(
    header=dict(
        values=list(df2.columns),
        fill_color='darkblue',
        align='left',
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[df2.Horário, df2.Segunda, df2.Terça, df2.Quarta, df2.Quinta, df2.Sexta],
        fill_color='lavender',
        align='left',
        font=dict(color='black', size=11),
        height=30
    )
)])

fig2.update_layout(
    title='Matérias que não fiz, estão fora do prazo 1 do 4º',
    width=800,
    height=400
)

# 4. Mostrar o gráfico
fig.show()

fig2.show()
