import plotly.graph_objects as go
import numpy as np

periodos = [
    'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
    'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 'Q1 2023', 'Q2 2023',
    'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024'
]

btc_purchased = [
    38250, 32220, 20856, 13758, 8957, 10350,
    4827, 480, 301, 2501, 6455, 13378,
    5912, 30905, 25095, 12095, 25889
]

amount_invested = [
    425.0, 700.0, 1086.0, 289.0, 419.0, 590.6,
    215.0, 10.0, 6.0, 68.25, 150.0, 376.3,
    161.7, 1214.3, 1636.9, 793.8, 1579.6
]

bitcoins_acumulados = [
    38250, 70470, 91326, 105085, 114042, 124391,
    129218, 129699, 130000, 132500, 138955, 152333,
    158245, 189150, 214246, 226331, 252220
]

amount_invested_numeric = np.array(amount_invested) * 1e6

btc_purchased = np.array(btc_purchased, dtype=np.int64)
bitcoins_acumulados = np.array(bitcoins_acumulados, dtype=np.int64)

valor_investido_acumulado = np.cumsum(amount_invested_numeric, dtype=np.float64)

preco_bitcoin_atual = 76000  # Preço atual do Bitcoin em US$
valor_atual_mercado_acumulado = bitcoins_acumulados.astype(np.float64) * preco_bitcoin_atual

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=periodos,
    y=valor_atual_mercado_acumulado,
    mode='lines+markers+text',
    name='Valor Atual de Mercado (US$)',
    line=dict(color='gold', width=4, dash='dash'),
    marker=dict(size=10),
    text=[f"${v / 1e9:.1f}B" for v in valor_atual_mercado_acumulado],
    textposition='top center',
    textfont=dict(size=19, color='white'),
    hovertemplate='Período: %{x}<br>Valor Atual de Mercado: %{text}'
))

fig.add_trace(go.Scatter(
    x=periodos,
    y=valor_investido_acumulado,
    mode='lines+markers+text',
    name='Valor Investido Acumulado (US$)',
    line=dict(color='blue', width=4),
    marker=dict(size=10),
    text=[f"${v / 1e9:.2f}B" if v >= 1e9 else f"${v / 1e6:.1f}M" for v in valor_investido_acumulado],
    textposition='top center',
    textfont=dict(size=19, color='white'),
    hovertemplate='Período: %{x}<br>Valor Investido Acumulado: %{text}'
))

fig.add_trace(go.Scatter(
    x=periodos,
    y=bitcoins_acumulados,
    mode='lines+markers+text',
    name='Bitcoins Acumulados',
    yaxis='y2',
    line=dict(color='green', width=4),
    marker=dict(size=10),
    text=[f"{v / 1e3:.1f}k" for v in bitcoins_acumulados],
    textposition='top center',
    textfont=dict(size=19, color='white'),
    hovertemplate='Período: %{x}<br>Bitcoins Acumulados: %{text}'
))

fig.update_layout(
    title='Crescimento do Patrimônio em Bitcoin da MicroStrategy',
    title_font=dict(size=35, family='Arial Black', color='white'),
    xaxis=dict(
        title='Trimestre',
        title_font=dict(size=19, color='white'),
        tickfont=dict(size=17, color='white'),
        showgrid=False,
        categoryorder='array',
        categoryarray=periodos
    ),
    yaxis=dict(
        title='Valor Investido e Valor de Mercado (US$)',
        title_font=dict(size=19, color='white'),
        tickfont=dict(size=17, color='white'),
        side='left',
        showgrid=False,
    ),
    yaxis2=dict(
        title='Quantidade de Bitcoins',
        title_font=dict(size=19, color='white'),
        tickfont=dict(size=17, color='white'),
        overlaying='y',
        side='right',
        range=[0, 300000],
        showgrid=False
    ),
    legend=dict(
        x=0.01, y=0.99,
        bgcolor='rgba(0, 0, 0, 0.5)',
        bordercolor='white',
        borderwidth=1,
        font=dict(size=25, color='white')
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    hovermode='x unified',
    width=1600,  # Definindo a largura da imagem
    height=900   # Definindo a altura da imagem
)

fig.show()

fig.write_image("microstrategy_bitcoin_growth.png", width=1600, height=900)

fig.write_html("microstrategy_bitcoin_growth.html")
