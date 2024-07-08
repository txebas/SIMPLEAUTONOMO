import streamlit as st
import pandas as pd
from fpdf import FPDF  # Librería para crear PDFs
from db_utils import obtener_ingresos

# Función para generar el PDF de la factura
def generar_factura(id_ingreso, fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Factura", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Fecha: {fecha}", ln=True)
    pdf.cell(200, 10, txt=f"Descripción: {descripcion}", ln=True)
    pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Importe: {importe}", ln=True)
    pdf.cell(200, 10, txt=f"Forma de pago: {forma_pago}", ln=True)
    pdf.cell(200, 10, txt=f"Número de factura: {numero_factura}", ln=True)
    pdf.cell(200, 10, txt=f"Categoría: {categoria}", ln=True)
    
    nombre_archivo = f"factura_{id_ingreso}.pdf"
    pdf.output(nombre_archivo)

# Configuración de la página
st.set_page_config(page_title="Facturas", page_icon="🧾")

st.subheader("Generar Facturas")

# Obtener lista de ingresos desde la base de datos
ingresos = obtener_ingresos()
print(ingresos)
print(type(ingresos))
ingresos_df = pd.DataFrame(ingresos, columns=["ID", "Fecha", "Descripción", "Cliente", "Importe", "Forma de pago", "Número de factura","Categoría"])

# Mostrar lista de ingresos para seleccionar uno para la factura
ingreso_seleccionado = st.selectbox("Selecciona un ingreso para generar la factura:", ingresos_df["ID"])

# Obtener detalles del ingreso seleccionado
detalle_ingreso = ingresos_df[ingresos_df["ID"] == ingreso_seleccionado].iloc[0]

# Mostrar detalles del ingreso seleccionado
st.write("Detalles del Ingreso Seleccionado:")
st.write(f"ID: {detalle_ingreso['ID']}")
st.write(f"Fecha: {detalle_ingreso['Fecha']}")
st.write(f"Descripción: {detalle_ingreso['Descripción']}")
st.write(f"Cliente: {detalle_ingreso['Cliente']}")
st.write(f"Importe: {detalle_ingreso['Importe']}")
st.write(f"Forma de pago: {detalle_ingreso['Forma de pago']}")
st.write(f"Número de factura: {detalle_ingreso['Número de factura']}")
st.write(f"Categoría: {detalle_ingreso['Categoría']}")

# Botón para generar la factura en PDF
if st.button("Generar Factura en PDF"):
    generar_factura(detalle_ingreso['ID'], str(detalle_ingreso['Fecha']), detalle_ingreso['Descripción'], detalle_ingreso['Cliente'], detalle_ingreso['Importe'], detalle_ingreso['Forma de pago'], detalle_ingreso['Número de factura'],detalle_ingreso['Categoría'])
    st.success(f"Factura generada correctamente. Puedes descargarla haciendo clic [aquí](factura_{detalle_ingreso['ID']}.pdf).")

