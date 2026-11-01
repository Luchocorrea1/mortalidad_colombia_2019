import pandas as pd
import os

print("Iniciando preprocesamiento de datos del DANE...")

# Rutas relativas a los archivos de la carpeta data
base_dir = os.path.dirname(os.path.abspath(__file__))
path_mortalidad = os.path.join(base_dir, '../data/Anexo1.NoFetal2019_CE_15-03-23.xlsx')
path_divipola = os.path.join(base_dir, '../data/Divipola_CE_.xlsx')
path_salida = os.path.join(base_dir, '../data/mortalidad_2019_limpio.csv')

# Cargar microdatos de mortalidad 2019
df_mortalidad = pd.read_excel(path_mortalidad, sheet_name='No_Fetales_2019')

# Cargar Divipola para nombres de departamentos y municipios
df_divipola = pd.read_excel(path_divipola, sheet_name='Hoja1')

# Normalizar códigos para cruces limpios
df_mortalidad['COD_DEPARTAMENTO'] = df_mortalidad['COD_DEPARTAMENTO'].astype(str).str.zfill(2)
df_mortalidad['COD_MUNICIPIO'] = df_mortalidad['COD_MUNICIPIO'].astype(str).str.zfill(5)
df_divipola['COD_DEPARTAMENTO'] = df_divipola['COD_DEPARTAMENTO'].astype(str).str.zfill(2)
df_divipola['COD_MUNICIPIO'] = df_divipola['COD_MUNICIPIO'].astype(str).str.zfill(5)

# Cruzar con Divipola
df_merged = pd.merge(
    df_mortalidad,
    df_divipola[['COD_DEPARTAMENTO', 'DEPARTAMENTO', 'COD_MUNICIPIO', 'MUNICIPIO']],
    on=['COD_DEPARTAMENTO', 'COD_MUNICIPIO'],
    how='left'
)

# Guardar archivo optimizado
df_merged.to_csv(path_salida, index=False)
print("¡Preprocesamiento finalizado con éxito! Archivo guardado en data/mortalidad_2019_limpio.csv")