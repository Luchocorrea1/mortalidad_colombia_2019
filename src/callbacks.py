from dash.dependencies import Input, Output
from dash import dash_table
import plotly.express as px
import pandas as pd
import os

# Cargar datos limpios
base_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(base_dir, '../data/mortalidad_2019_limpio.csv')

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.DataFrame()

def registrar_callbacks(app):
    @app.callback(
        [
            Output('grafico-departamentos', 'figure'),
            Output('grafico-lineas-mes', 'figure'),
            Output('grafico-homicidios', 'figure'),
            Output('grafico-circular', 'figure'),
            Output('grafico-barras-apiladas', 'figure'),
            Output('grafico-histograma-edad', 'figure'),
            Output('tabla-causas-container', 'children')
        ],
        [Input('grafico-departamentos', 'id')]
    )
    def actualizar_dashboard(_):
        if df.empty:
            fig_vacia = px.scatter(title="Sin datos disponibles. Ejecute preprocesar.py")
            return fig_vacia, fig_vacia, fig_vacia, fig_vacia, fig_vacia, fig_vacia, "No hay datos."
        
        # 1. Total de muertes por departamento
        df_dep = df.groupby(['COD_DEPARTAMENTO', 'DEPARTAMENTO']).size().reset_index(name='Total_Muertes')
        fig_dep = px.bar(df_dep.sort_values(by='Total_Muertes', ascending=False), 
                         x='DEPARTAMENTO', y='Total_Muertes', 
                         title="Distribución Total de Muertes por Departamento (2019)",
                         color='Total_Muertes', template='plotly_white')
        
        # 2. Total de muertes por mes
        df_mes = df.groupby('MES').size().reset_index(name='Total_Muertes')
        meses_nombres = {1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun', 
                         7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'}
        df_mes['Mes_Nombre'] = df_mes['MES'].map(meses_nombres)
        fig_mes = px.line(df_mes, x='Mes_Nombre', y='Total_Muertes', markers=True,
                          title="Evolución del Total de Muertes por Mes",
                          template='plotly_white')
        
        # 3. Top 5 ciudades más violentas (Homicidios Cód. X95)
        if 'COD_MUERTE' in df.columns:
            df_homicidios = df[df['COD_MUERTE'].astype(str).str.contains('X95', na=False)]
        else:
            df_homicidios = pd.DataFrame()
            
        if not df_homicidios.empty:
            df_ciudades_hom = df_homicidios.groupby(['COD_MUNICIPIO', 'MUNICIPIO']).size().reset_index(name='Homicidios')
            top_5_hom = df_ciudades_hom.sort_values(by='Homicidios', ascending=False).head(5)
        else:
            top_5_hom = pd.DataFrame({'MUNICIPIO': ['Sin registros X95'], 'Homicidios': [0]})
            
        fig_hom = px.bar(top_5_hom, x='MUNICIPIO', y='Homicidios',
                         title="Top 5 Ciudades con Mayor Homicidios (Cód. X95)",
                         color='Homicidios', template='plotly_white')
        
        # 4. Top 10 ciudades con menor índice de mortalidad
        df_ciudades_mort = df.groupby('MUNICIPIO').size().reset_index(name='Total_Muertes')
        bottom_10 = df_ciudades_mort.sort_values(by='Total_Muertes', ascending=True).head(10)
        fig_circ = px.pie(bottom_10, names='MUNICIPIO', values='Total_Muertes',
                          title="Top 10 Ciudades con Menor Índice de Mortalidad",
                          template='plotly_white')
        
        # 5. Tabla de principales causas de muerte
        if 'COD_MUERTE' in df.columns:
            df_causas = df.groupby('COD_MUERTE').size().reset_index(name='Total_Casos')
            top_10_causas = df_causas.sort_values(by='Total_Casos', ascending=False).head(10)
        else:
            top_10_causas = pd.DataFrame(columns=['COD_MUERTE', 'Total_Casos'])
            
        tabla_componente = dash_table.DataTable(
            data=top_10_causas.to_dict('records'),
            columns=[{"name": "Código Causa de Muerte", "id": "COD_MUERTE"}, {"name": "Total de Casos", "id": "Total_Casos"}],
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_header={'backgroundColor': '#2c3e50', 'color': 'white', 'fontWeight': 'bold'},
            style_cell={'textAlign': 'center', 'padding': '8px'}
        )
        
        # 6. Gráfico de barras apiladas por sexo
        if 'SEXO' in df.columns and 'DEPARTAMENTO' in df.columns:
            df_sexo = df.groupby(['DEPARTAMENTO', 'SEXO']).size().reset_index(name='Total')
            df_sexo['Sexo_Label'] = df_sexo['SEXO'].map({1: 'Masculino', 2: 'Femenino', 3: 'Indeterminado'})
        else:
            df_sexo = pd.DataFrame(columns=['DEPARTAMENTO', 'Total', 'Sexo_Label'])
            
        fig_apiladas = px.bar(df_sexo, x='DEPARTAMENTO', y='Total', color='Sexo_Label',
                              title="Comparación de Muertes por Sexo y Departamento",
                              barmode='stack', template='plotly_white')
        
        # 7. Histograma de grupos de edad
        if 'GRUPO_EDAD1' in df.columns:
            fig_hist = px.histogram(df, x='GRUPO_EDAD1', nbins=20,
                                    title="Distribución de Muertes por Grupo de Edad (GRUPO_EDAD1)",
                                    template='plotly_white')
            fig_hist.update_layout(xaxis_title="Código Grupo de Edad DANE", yaxis_title="Total Muertes")
        else:
            fig_hist = px.scatter(title="Variable GRUPO_EDAD1 no encontrada")

        return fig_dep, fig_mes, fig_hom, fig_circ, fig_apiladas, fig_hist, tabla_componente