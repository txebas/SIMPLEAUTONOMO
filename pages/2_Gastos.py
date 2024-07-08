import streamlit as st
import pandas as pd
from datetime import datetime
from db_utils import agregar_gasto, obtener_gastos, actualizar_gasto, eliminar_gasto

st.set_page_config(page_title="Gastos", page_icon="💸")

st.subheader("Gastos")
with st.form(key='gasto_form'):
    # fecha = st.date_input("Fecha")
    # proveedor = st.text_input("Proveedor")
    # importe = st.number_input("Importe", min_value=0.0)
    # forma_pago = st.selectbox("Forma de pago", ["Efectivo", "Transferencia bancaria", "Tarjeta de crédito", "Otro"])
    # factura_ticket = st.text_input("Factura o Ticket")
    # categoria = st.text_input("Categoría")

        # Arrange form elements in a single row using st.columns()
    col1, col2, col3 = st.columns(3)

    # Add form fields to each column
    with col1:
        proveedor = st.text_input("Proveedor")
        categoria = st.text_input("Categoría")


    with col2:
        importe = st.number_input("Importe", min_value=0.0)
        forma_pago = st.selectbox("Forma de pago", ["Efectivo", "Transferencia bancaria", "Tarjeta de crédito", "Otro"])
    
    with col3:
        fecha = st.date_input("Fecha")
        factura_ticket = st.text_input("Factura o Ticket")


    descripcion = st.text_input("Descripción")

    submit_button = st.form_submit_button(label='Agregar Gasto')

    if submit_button:
        agregar_gasto(fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria)
        st.success("Gasto agregado correctamente")

st.subheader("Lista de Gastos")
gastos = obtener_gastos()
gastos_df = pd.DataFrame(gastos, columns=["ID", "Fecha", "Descripción", "Proveedor", "Importe", "Forma de pago", "Factura o Ticket", "Categoría"])
gastos_df['Fecha'] = pd.to_datetime(gastos_df['Fecha'])

edited_df = st.data_editor(gastos_df, num_rows="dynamic")

if st.button('Guardar Cambios'):
    for i, row in edited_df.iterrows():
        if not (row == gastos_df.loc[i]).all():
            actualizar_gasto(row['ID'], row['Fecha'].date(), row['Descripción'], row['Proveedor'], row['Importe'], row['Forma de pago'], row['Factura o Ticket'], row['Categoría'])
    st.success("Gastos actualizados correctamente")
    st.experimental_rerun()
