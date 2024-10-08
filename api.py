# api.py
from flask import Flask, jsonify
from controlador_productos import obtener_productos

app = Flask(__name__)

# Ruta para obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def api_obtener_productos():
    productos = obtener_productos()
    if productos:
        return jsonify(productos)
    else:
        return jsonify({"mensaje": "No se encontraron productos"}), 404

if __name__ == '__main__':
    app.run(debug=True)
