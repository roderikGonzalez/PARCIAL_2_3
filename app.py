import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd

# Título de la aplicación
st .title("Hello, I´m Roderik")
st .write("Welcome to your first Streamlit app.")

# Cargar las variables del archivo .env
load_dotenv()

# Obtener valores
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Conexión a MySQL (Railway)
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Función para obtener una tabla
def obtener_tabla():
    conexion = get_connection()
    query = f"SELECT * FROM tabla_prueba;"
    df = pd.read_sql(query, conexion,)
    conexion.close()
    return df

# Interfaz Streamlit
st.title("Visualizador de Tablas - Railway DB")

if st.button("Mostrar tabla"):
    try:
        datos = obtener_tabla().reset_index(drop=True)
        st.success("Tabla obtenida correctamente.")
        st.dataframe(datos, use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

