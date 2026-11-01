from dash import Dash
from .layout import crear_layout
from .callbacks import registrar_callbacks

app = Dash(__name__)
server = app.server  # Obligatorio para Render (Gunicorn buscará src.app:server)[cite: 59, 61]

# Asignar el layout
app.layout = crear_layout()

# Registrar los callbacks
registrar_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)