import streamlit as st
import pandas as pd
from datetime import datetime
from db_utils import obtener_ingresos, obtener_gastos

st.set_page_config(page_title="Informes", page_icon="📊")

st.subheader("Informes")
st.write("Generar informes de ingresos y gastos")

start_date = st.date_input("Fecha de inicio")
end_date = st.date_input("Fecha de fin")

if st.button("Generar Informe"):
    ingresos = obtener_ingresos()
    gastos = obtener_gastos()

    ingresos_df = pd.DataFrame(ingresos, columns=["ID", "Fecha", "Descripción", "Cliente", "Importe", "Forma de pago", "Número de factura", "Categoría"])
    gastos_df = pd.DataFrame(gastos, columns=["ID", "Fecha", "Descripción", "Proveedor", "Importe", "Forma de pago", "Factura o Ticket", "Categoría"])

    ingresos_df['Fecha'] = pd.to_datetime(ingresos_df['Fecha'])
    gastos_df['Fecha'] = pd.to_datetime(gastos_df['Fecha'])

    ingresos_filtrados = ingresos_df[(ingresos_df['Fecha'] >= pd.to_datetime(start_date)) & (ingresos_df['Fecha'] <= pd.to_datetime(end_date))]
    gastos_filtrados = gastos_df[(gastos_df['Fecha'] >= pd.to_datetime(start_date)) & (gastos_df['Fecha'] <= pd.to_datetime(end_date))]

    st.subheader("Ingresos")
    st.dataframe(ingresos_filtrados)

    st.subheader("Gastos")
    st.dataframe(gastos_filtrados)

    total_ingresos = ingresos_filtrados['Importe'].sum()
    total_gastos = gastos_filtrados['Importe'].sum()

    st.write(f"Total Ingresos: {total_ingresos}")
    st.write(f"Total Gastos: {total_gastos}")
    st.write(f"Balance: {total_ingresos - total_gastos}")

    percent=((total_ingresos-total_gastos)/total_ingresos)*100
    col1, col2, col3 = st.columns(3)
    #col1.metric("Temperature", "70 °F", "1.2 °F")
    col1.metric("Total",str(percent)+'%')
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
