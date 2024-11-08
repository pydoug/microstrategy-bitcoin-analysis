import plotly.graph_objects as go
import numpy as np

# Dados dos períodos (trimestres)
periodos = [
    'Q3 2020', 'Q4 2020', 'Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021',
    'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 'Q1 2023', 'Q2 2023',
    'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024'
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

valor_investido_acumulado = np.cumsum(amount_invested_numeric, dtype=np.float64)

preco_bitcoin_atual = 76000  
valor_atual_mercado_acumulado = np.array(bitcoins_acumulados, dtype=np.float64) * preco_bitcoin_atual


lucro_intrinseco = valor_atual_mercado_acumulado - valor_investido_acumulado

print("\n=== DADOS CALCULADOS ===")
print("Períodos:", periodos)
print("Valor Investido Acumulado (US$):", valor_investido_acumulado)
print("Valor Atual de Mercado Acumulado (US$):", valor_atual_mercado_acumulado)
print("Lucro Intrínseco (US$):", lucro_intrinseco)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=periodos,
    y=valor_investido_acumulado,
    mode='lines',
    line=dict(color='red'),
    fill='tozeroy',
    fillcolor='rgba(255, 0, 0, 0.7)',
    name='Valor Investido em BTC',
    hovertemplate='Período: %{x}<br>Valor Investido: %{y:$,.2f}',
    showlegend=True
))

fig.add_trace(go.Scatter(
    x=periodos,
    y=valor_atual_mercado_acumulado,
    mode='lines',
    line=dict(color='lime'),
    fill='tonexty',
    fillcolor='rgba(0, 255, 0, 0.7)',  # Verde mais forte
    name='Valor de Mercado $76.000',
    hovertemplate='Período: %{x}<br>Valor de Mercado: %{y:$,.2f}',
    showlegend=True
))

fig.add_trace(go.Scatter(
    x=periodos,
    y=lucro_intrinseco,
    mode='lines+markers+text',
    line=dict(color='blue', dash='dash'),
    marker=dict(size=6),
    name='Lucro Intrínseco',
    text=[f"${v/1e9:.2f}B" if v >= 1e9 else f"${v/1e6:.0f}M" for v in lucro_intrinseco],
    textposition='top center',
    textfont=dict(size=17, color='white'),
    hovertemplate='Período: %{x}<br>Lucro Intrínseco: %{y:$,.2f}',
    showlegend=True
))

fig.update_layout(
    title='Análise do Investimento da MicroStrategy em Bitcoin',
    title_font=dict(size=35, family='Arial Black', color='white'),
    xaxis=dict(
        title='Trimestre',
        title_font=dict(size=19, color='white'),
        tickfont=dict(size=17, color='white'),
        showgrid=False,
        categoryorder='array',
        categoryarray=periodos,
        showline=False,
        zeroline=False
    ),
    yaxis=dict(
        title='Valores (US$)',
        title_font=dict(size=19, color='white'),
        tickfont=dict(size=17, color='white'),
        showgrid=False,
        range=[-1e9, 2e10], 
    ),
    legend=dict(
        x=0.01, y=0.99,
        bgcolor='rgba(0, 0, 0, 0.5)',
        bordercolor='white',
        borderwidth=1,
        font=dict(size=25, color='white')
    ),
    hovermode='x unified',
    width=1600,
    height=900,
    plot_bgcolor='black',
    paper_bgcolor='black',
)

fig.update_xaxes(showline=False, zeroline=False)
fig.update_yaxes(showline=False, zeroline=False)

fig.show()

fig.write_image("microstrategy_investment_analysis.png", width=1600, height=900)

fig.write_html("microstrategy_graph_data.html")
