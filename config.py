# config.py
import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="proveedores"
    )
