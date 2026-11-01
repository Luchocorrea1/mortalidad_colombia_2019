# Aplicación Web Interactiva para el Análisis de Mortalidad en Colombia (2019)

**Maestría en Inteligencia Artificial — Aplicaciones I (Actividad 4)**  
**Integrantes del Grupo:** 
* Cristhian Camilo Gutiérrez Bejarano[cite: 1]
* Luis Norbey Correa Diaz[cite: 1]

---

## 1. Introducción del Proyecto
Esta aplicación web interactiva ha sido desarrollada en el lenguaje de programación Python utilizando los frameworks avanzados **Dash** y **Plotly**[cite: 1]. Su propósito principal es transformar un conjunto de datos complejos y masivos en representaciones visuales dinámicas e intuitivas, permitiendo explorar a profundidad los patrones, tendencias y correlaciones clave de la mortalidad en Colombia durante el año 2019[cite: 1].

## 2. Objetivo
Analizar la distribución espacial, demográfica y temporal de la mortalidad en Colombia para el año 2019 mediante un dashboard web interactivo, facilitando la identificación de factores críticos como los índices departamentales de defunciones, la evolución mensual, la incidencia de homicidios por ciudades, las principales causas de muerte y la distribución etaria a lo largo del ciclo vital[cite: 1].

## 3. Estructura del Proyecto
El proyecto está organizado de manera modular siguiendo las mejores prácticas de desarrollo de software y estándares de arquitectura en Python:
```text
mortalidad_colombia_2019/
├── data/
│   ├── Anexo1.NoFetal2019_CE_15-03-23.xlsx   # Microdatos originales de mortalidad DANE
│   ├── Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx # Catálogo de patologías CIE-10
│   ├── Divipola_CE_.xlsx                    # División político-administrativa
│   └── mortalidad_2019_limpio.csv           # Datos optimizados para el dashboard
├── src/
│   ├── app.py                               # Punto de entrada principal y servidor Flask
│   ├── layout.py                            # Definición de la interfaz visual y componentes
│   ├── callbacks.py                         # Lógica de interactividad y gráficos
│   └── preprocesar.py                       # Script de limpieza y estructuración de datos
├── venv/                                    # Entorno virtual de Python (aislado)
├── .gitignore                               # Archivos excluidos del control de versiones
├── README.md                                # Documentación técnica del proyecto
└── requirements.txt                         # Dependencias y librerías del proyecto

```

## 4. Requisitos y Dependencias

Para garantizar el funcionamiento óptimo de la aplicación, se requiere el uso de Python (versión 3.9 o superior) y las siguientes librerías principales especificadas en el archivo `requirements.txt`:

* `dash >= 2.0.0`
* `plotly >= 5.0.0`
* `pandas >= 1.3.0`
* `openpyxl >= 3.0.0`
* `gunicorn >= 20.1.0` (servidor WSGI para producción)

## 5. Software y Herramientas Utilizadas

* **Lenguaje de Programación:** Python.


* **Framework Web y Analítico:** Dash (basado en Flask y React).


* **Visualización de Datos:** Plotly Express.


* **Manipulación de Datos:** Pandas.
* **Entorno de Desarrollo:** Visual Studio Code.
* **Control de Versiones:** Git y GitHub.
* **Plataforma como Servicio (PaaS):** Render.



## 6. Instalación y Ejecución Local

Sigue estos pasos para clonar el repositorio y ejecutar la aplicación de forma local en tu máquina:

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Luchocorrea1/mortalidad_colombia_2019.git
cd mortalidad_colombia_2019

```


2. **Crear y activar un entorno virtual:**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

```


3. **Instalar las dependencias:**
```bash
pip install -r requirements.txt

```


4. **Ejecutar el preprocesamiento de datos (si es necesario):**
```bash
python src/preprocesar.py

```


5. **Ejecutar la aplicación localmente:**
```bash
python src/app.py

```


*Abre tu navegador web e ingresa a la dirección local generada (por defecto: `http://127.0.0.1:8050/`).*

## 7. Despliegue en la Nube (Render)

La aplicación ha sido desplegada en una plataforma como servicio (PaaS) utilizando **Render**, garantizando accesibilidad pública en línea:

1. Conectar el repositorio de GitHub a un nuevo *Web Service* en Render.


2. Configurar el comando de construcción (*Build Command*): `pip install -r requirements.txt`.


3. Configurar el comando de inicio (*Start Command*): `gunicorn src.app:server`.


4. Enlace público de la aplicación desplegada: [Insertar URL de Render aquí]



## 8. Visualizaciones y Resultados

A continuación se presentan los componentes visuales interactivos implementados en el dashboard:

* **Distribución de Muertes por Departamento:** Permite identificar visualmente las regiones del país con mayor concentración de defunciones durante el año 2019.


*(Inserta aquí tu captura de pantalla del gráfico de barras departamental)*
* **Evolución Temporal por Mes:** Muestra las variaciones estacionales y los picos de mortalidad a lo largo de los meses del año.


*(Inserta aquí tu captura de pantalla del gráfico de líneas)*
* **Índice de Homicidios (Top 5 Ciudades):** Destaca las ciudades con mayor concentración de muertes violentas asociadas a agresiones con armas de fuego (códigos específicos analizados).


*(Inserta aquí tu captura de pantalla del gráfico de barras de homicidios)*
* **Menor Índice de Mortalidad (Top 10 Ciudades):** Ilustra mediante un diagrama circular las regiones que registraron los menores índices de defunciones.


*(Inserta aquí tu captura de pantalla del gráfico circular)*
* **Principales Causas de Muerte (Tabla Resumen):** Lista ordenada de mayor a menor frecuencia de las 10 principales patologías o causas asociadas a los decesos.


*(Inserta aquí tu captura de pantalla de la tabla interactiva)*
* **Análisis Demográfico por Sexo y Edad:** Comparativa de género por departamento y distribución etaria según los rangos del DANE a lo largo del ciclo vital.


*(Inserta aquí tus capturas de pantalla de las barras apiladas y el histograma de edades)*

```

```