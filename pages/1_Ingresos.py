import streamlit as st
import pandas as pd
from datetime import datetime
from db_utils import agregar_ingreso, obtener_ingresos, actualizar_ingreso, eliminar_ingreso

st.set_page_config(page_title="Ingresos", page_icon="💰")

st.subheader("Ingresos")
with st.form(key='ingreso_form'):
    # fecha = st.date_input("Fecha")
    # descripcion = st.text_input("Descripción")
    # cliente = st.text_input("Cliente")
    # importe = st.number_input("Importe", min_value=0.0)
    # forma_pago = st.selectbox("Forma de pago", ["Efectivo", "Transferencia bancaria", "Tarjeta de crédito", "Otro"])
    # numero_factura = st.text_input("Número de factura")
    # categoria = st.text_input("Categoría")
    # submit_button = st.form_submit_button(label='Agregar Ingreso')
    # Arrange form elements in a single row using st.columns()
    col1, col2, col3 = st.columns(3)

    # Add form fields to each column
    with col1:
        numero_factura = st.text_input("Número de factura")
        categoria = st.text_input("Categoría")
        

    with col2:
        importe = st.number_input("Importe", min_value=0.0)
        forma_pago = st.selectbox("Forma de pago", ["Efectivo", "Transferencia bancaria", "Tarjeta de crédito", "Otro"])
        

    with col3:
        fecha = st.date_input("Fecha")
        cliente = st.text_input("Cliente")
    descripcion = st.text_input("Descripción")
    submit_button = st.form_submit_button(label='Agregar Ingreso')

    if submit_button:
        agregar_ingreso(fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria)
        st.success("Ingreso agregado correctamente")

st.subheader("Lista de Ingresos")
ingresos = obtener_ingresos()
ingresos_df = pd.DataFrame(ingresos, columns=["ID", "Fecha", "Descripción", "Cliente", "Importe", "Forma de pago", "Número de factura", "Categoría"])
ingresos_df['Fecha'] = pd.to_datetime(ingresos_df['Fecha'])

edited_df = st.data_editor(ingresos_df.copy(), num_rows="dynamic")

if st.button('Guardar Cambios'):
    print("Guardar Cambios")
    st.success("Ingresos actualizados correctamente")

    for i, row in edited_df.iterrows():
        print("x")
        print("i",i,"row=",row)
        original_row = ingresos_df.loc[ingresos_df['ID'] == row['ID']]
        if original_row.empty:
            actualizar_ingreso(row['ID'], row['Fecha'].date(), row['Descripción'], row['Cliente'], row['Importe'], row['Forma de pago'], row['Número de factura'], row['Categoría'])
        if not original_row.empty and not (row == original_row.iloc[0]).all():
            actualizar_ingreso(row['ID'], row['Fecha'].date(), row['Descripción'], row['Cliente'], row['Importe'], row['Forma de pago'], row['Número de factura'], row['Categoría'])
    print("hola")
    st.success("Ingresos actualizados correctamente")
    st.rerun()
    print(st.session_state['edited_df'])
    
