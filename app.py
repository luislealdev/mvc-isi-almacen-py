# app.py
from flask import Flask, render_template
from controlador_productos import obtener_productos, agrupar_por_unidad

app = Flask(__name__)

# Ruta para mostrar la tabla de productos
@app.route('/productos')
def vista_tabla_productos():
    productos = obtener_productos()  # Obtener productos desde el controlador
    return render_template('vista_tabla_productos.html', productos=productos)

# Ruta para mostrar el histograma de productos
@app.route('/productos/grafica')
def vista_grafica_productos():
    resultados = agrupar_por_unidad()
    unidades = [row['unidad'] for row in resultados]
    cantidades = [row['total'] for row in resultados]
    return render_template('vista_grafica_productos.html', unidades=unidades, cantidades=cantidades)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
