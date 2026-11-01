from dash import html, dcc, dash_table

def crear_layout():
    return html.Div([
        html.H1("Análisis de Mortalidad en Colombia (2019)", style={'textAlign': 'center', 'color': '#2c3e50'}),
        html.P("Maestría en Inteligencia Artificial - Aplicaciones I (Actividad 4)", style={'textAlign': 'center', 'color': '#7f8c8d'}),
        
        html.Div([
            # 1. Gráfico de barras por departamento
            html.Div([dcc.Graph(id='grafico-departamentos')], style={'width': '100%', 'padding': '10px'}),
            
            # 2. Gráfico de líneas por mes
            html.Div([dcc.Graph(id='grafico-lineas-mes')], style={'width': '50%', 'display': 'inline-block'}),
            
            # 3. Gráfico de barras de homicidios (Top 5 ciudades más violentas)
            html.Div([dcc.Graph(id='grafico-homicidios')], style={'width': '50%', 'display': 'inline-block'}),
            
            # 4. Gráfico circular (Top 10 ciudades con menor mortalidad)
            html.Div([dcc.Graph(id='grafico-circular')], style={'width': '50%', 'display': 'inline-block'}),
            
            # 6. Gráfico de barras apiladas por sexo y departamento
            html.Div([dcc.Graph(id='grafico-barras-apiladas')], style={'width': '50%', 'display': 'inline-block'}),
            
            # 7. Histograma de grupos de edad
            html.Div([dcc.Graph(id='grafico-histograma-edad')], style={'width': '100%', 'padding': '10px'}),
            
            # 5. Tabla de principales causas de muerte
            html.Div([
                html.H3("Top 10 Principales Causas de Muerte en Colombia", style={'textAlign': 'center'}),
                html.Div(id='tabla-causas-container')
            ], style={'width': '100%', 'padding': '20px'})
        ])
    ])