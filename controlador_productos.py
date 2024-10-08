# controlador_productos.py
import mysql.connector
from config import obtener_conexion

def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return productos

def agrupar_por_unidad():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT unidad, SUM(cantidad) AS total FROM productos GROUP BY unidad")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados
