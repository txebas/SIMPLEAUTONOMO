import streamlit as st
from db_utils import init_db

st.set_page_config(
    page_title="Registro de Ingresos y Gastos para Autónomos",
    page_icon="💰",
    layout="wide",
)

st.title("Registro de Ingresos y Gastos para Autónomos")

st.write("""
    Bienvenido a la aplicación de registro de ingresos y gastos para autónomos. 
    Utilice el menú de la izquierda para navegar entre las páginas.
""")

init_db()
