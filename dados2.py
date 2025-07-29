import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import plotly.express as px

#dataframe
df = pd.read_csv("C:/Users/bruno/PROJETOS PYTHON/projetos/analysis_data/ecommerce_estatistica.csv")

# criação dos gráficos com Plotly Express
#histograma
fig_hist = px.histogram(df, x='Preço', nbins=30, title='Distribuição dos Preços',
                        labels={'Preço': 'Preço'}, color_discrete_sequence=['blue'])
# Scatter Plot
fig_scatter = px.scatter(df, x='Desconto', y='Preço', title='Relação entre Descontos e Preços',
                         labels={'Desconto': 'Desconto', 'Preço': 'Preço'}, 
                         color_discrete_sequence=['blue'])
# Mapa de calor
fig_heatmap = px.imshow(
    df.select_dtypes(include=[np.number]).corr(),
    title='Mapa de Calor das Correlações',
    color_continuous_scale='RdBu'
)
# Gráfico de barras
fig_bar = px.bar(df, x='Marca', y='Nota_MinMax', title='Marca por Nota Normalizada',
                 labels={'Marca': 'Marca', 'Nota_MinMax': 'Nota Normalizada'},
                 color_discrete_sequence=['blue'])
# Gráfico de pizza
fig_pie = px.pie(
    df,
    names='Temporada',
    title='Distribuição de Temporadas',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
# Gráfico de Densidade (KDE)
fig_density = px.density_contour(df, x='Preço', title='Densidade dos Preços',
                                  labels={'Preço': 'Preço'}, color_discrete_sequence=['blue'])
# Gráfico de regressão
fig_regression = px.scatter(df, x='Desconto', y='Preço', trendline  ='ols', 
                            title='Regressão entre Desconto e Preço',
                            labels={'Desconto': 'Desconto', 'Preço': 'Preço'},
                            color_discrete_sequence=['red'])


# Criação do aplicativo Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Análise de Dados de E-commerce"),
    dcc.Graph(
        id='histograma-precos',
        figure=px.histogram(df, x='Preço', nbins=30, title='Distribuição dos Preços', 
                            labels={'Preço': 'Preço'}, color_discrete_sequence=['blue'])
    ),
    dcc.Graph(
        id='scatter-desconto-preco',
        figure=px.scatter(df, x='Desconto', y='Preço', title='Relação entre Descontos e Preços',
                          labels={'Desconto': 'Desconto', 'Preço': 'Preço'}, 
                          color_discrete_sequence=['blue'])
    ),
    dcc.Graph(
        id='mapa-calor-correlacoes',
        figure=px.imshow(
            df.select_dtypes(include=[np.number]).corr(),
            title='Mapa de Calor das Correlações',
            color_continuous_scale='RdBu'
        )
    ),
    dcc.Graph(
        id='grafico-barras-marca',
        figure=px.bar(df, x='Marca', y='Nota_MinMax', title='Marca por Nota Normalizada',
                      labels={'Marca': 'Marca', 'Nota_MinMax': 'Nota Normalizada'},
                      color_discrete_sequence=['blue'])
    ),
    dcc.Graph(
        id='grafico-pizza-temporada',
        figure=px.pie(
            df,
            names='Temporada',
            title='Distribuição de Temporadas',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
    ), 
    dcc.Graph(
        id='grafico-densidade-precos',
        figure=px.density_contour(df, x='Preço', title='Densidade dos Preços',
                                  labels={'Preço': 'Preço'}, color_discrete_sequence=['blue'])
    ),
    dcc.Graph(
        id='grafico-regressao',
        figure=px.scatter(df, x='Desconto', y='Preço', trendline='ols', 
                          title='Regressão entre Desconto e Preço',
                          labels={'Desconto': 'Desconto', 'Preço': 'Preço'},
                          color_discrete_sequence=['red'])
    )
])   

# Executando o app
if __name__ == '__main__':
    app.run(debug=True)
