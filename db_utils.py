import sqlite3

def init_db():
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ingresos (
                    id INTEGER PRIMARY KEY,
                    fecha TEXT,
                    descripcion TEXT,
                    cliente TEXT,
                    importe REAL,
                    forma_pago TEXT,
                    numero_factura TEXT,
                    categoria TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS gastos (
                    id INTEGER PRIMARY KEY,
                    fecha TEXT,
                    descripcion TEXT,
                    proveedor TEXT,
                    importe REAL,
                    forma_pago TEXT,
                    factura_ticket TEXT,
                    categoria TEXT
                )''')
    conn.commit()
    conn.close()

def agregar_ingreso(fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('''INSERT INTO ingresos (fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', (fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria))
    conn.commit()
    conn.close()

def agregar_gasto(fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('''INSERT INTO gastos (fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''', (fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria))
    conn.commit()
    conn.close()

def obtener_ingresos():
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ingresos')
    ingresos = c.fetchall()
    conn.close()
    return ingresos

def obtener_gastos():
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM gastos')
    gastos = c.fetchall()
    conn.close()
    return gastos

""" def actualizar_ingreso(id, fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('''UPDATE ingresos SET fecha = ?, descripcion = ?, cliente = ?, importe = ?, forma_pago = ?, numero_factura = ?, categoria = ?
                 WHERE id = ?''', (fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria, id))
    conn.commit()
    conn.close()
 """

def actualizar_ingreso(id, fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()

    # Verificar si el id existe en la tabla ingresos
    c.execute('SELECT COUNT(*) FROM ingresos WHERE id = ?', (id,))
    existe = c.fetchone()[0]
    print("existe=",existe)
    if existe:
        # Actualizar el registro existente
        c.execute('''UPDATE ingresos 
                     SET fecha = ?, descripcion = ?, cliente = ?, importe = ?, 
                         forma_pago = ?, numero_factura = ?, categoria = ?
                     WHERE id = ?''',
                  (fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria, id))
    else:
        print('inserta')
        # Insertar un nuevo registro si el id no existe
        c.execute('''INSERT INTO ingresos (id, fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (id, fecha, descripcion, cliente, importe, forma_pago, numero_factura, categoria))

    conn.commit()
    conn.close()


def actualizar_gasto(id, fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('''UPDATE gastos SET fecha = ?, descripcion = ?, proveedor = ?, importe = ?, forma_pago = ?, factura_ticket = ?, categoria = ?
                 WHERE id = ?''', (fecha, descripcion, proveedor, importe, forma_pago, factura_ticket, categoria, id))
    conn.commit()
    conn.close()

def eliminar_ingreso(id):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('DELETE FROM ingresos WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def eliminar_gasto(id):
    conn = sqlite3.connect('finanzas_autonomo.db')
    c = conn.cursor()
    c.execute('DELETE FROM gastos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
