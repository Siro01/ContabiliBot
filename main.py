import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

# Creo el libro de Excel
wb = Workbook()
#Hoja activa de nuestro archivo excel
ws = wb.active
#Creamos las columas que vamos a usar en nuestro excel.
ws.append(["Fecha", "TIPO DE COMPROBANTE", "NRO DE PUNTO DE VENTA", "NUMERO DE COMPROBANTE", "RAZON SOCIAL", "CUIT","MONTO NETO", "IVA 21%", "TOTAL"])

def guardar_datos():
    fecha = entry_fecha.get().strip()
    comprobante = entry_comprobante.get().strip()
    venta = entry_venta.get().strip()
    n_comprobante = entry_NComprobante.get().strip()
    r_social = entry_RSocial.get().strip()
    cuit = entry_Cuit.get().strip()
    m_neto = entry_Neto.get().strip()
    iva = entry_Iva.get().strip()
    total = entry_Total.get().strip()

    # Imprimir los valores para verificar que no estén vacíos
    print(f"Fecha: '{fecha}'")
    print(f"Comprobante: '{comprobante}'")
    print(f"Venta: '{venta}'")
    print(f"Numero Comprobante: '{n_comprobante}'")
    print(f"Razon Social: '{r_social}'")
    print(f"CUIT: '{cuit}'")
    print(f"Monto Neto: '{m_neto}'")
    print(f"IVA: '{iva}'")
    print(f"Total: '{total}'")

    # Verificación de si hay algún campo vacío después de eliminar espacios
    if not all([fecha, comprobante, venta, n_comprobante, r_social, cuit, m_neto, iva, total]):
        print("¡Hay un campo vacío!")
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return
    print("¡Todos los campos están llenos!")

    try:
        venta = int(venta)
        n_comprobante = int(n_comprobante)
        cuit = int(cuit)
        m_neto = int(m_neto)
        iva = int(iva)
        total = int(total)
    except ValueError:
        messagebox.showwarning("Advertencia", "Fecha, Nro de Punto de Venta, Nro Comprobante, Cuit, Monto Neto,"
                                              " Iva y total deben ser numeros")
        return
    ws.append([fecha, comprobante, venta, n_comprobante, r_social, cuit, m_neto, iva, total])
    wb.save('client.xlsx')
    messagebox.showinfo("Informacion", "Datos guardados con exito")




root = tk.Tk()
root.title("Formulario de entrada de Datos")
root.configure(bg='#4B6587')
label_style = {"bg": '#4B6587', "fg": "white"}
entry_style = {"bg": '#D3D3D3', "fg": "black"}

#Columnas para los datos a ingresar.
label_fecha = tk.Label(root, text="Fecha", **label_style)
label_fecha.grid(row=0, column=0, padx=10, pady=5)
entry_fecha = tk.Entry(root, **entry_style)
entry_fecha.grid(row=0, column=1, padx=10, pady=5)

label_comprobante = tk.Label(root, text="TIPO DE COMPROBANTE", **label_style)
label_comprobante.grid(row=1, column=0, padx=10, pady=5)
entry_comprobante = tk.Entry(root, **entry_style)
entry_comprobante.grid(row=1, column=1, padx=10, pady=5)

label_venta = tk.Label(root, text="NRO DE PUNTO DE VENTA", **label_style)
label_venta.grid(row=2, column=0, padx=10, pady=5)
entry_venta = tk.Entry(root, **entry_style)
entry_venta.grid(row=2, column=1, padx=10, pady=5)

label_NComprobante = tk.Label(root, text="NUMERO DE COMPROBANTE", **label_style)
label_NComprobante.grid(row=3, column=0, padx=10, pady=5)
entry_NComprobante = tk.Entry(root, **entry_style)
entry_NComprobante.grid(row=3, column=1, padx=10, pady=5)

label_RSocial = tk.Label(root, text="RAZON SOCIAL", **label_style)
label_RSocial.grid(row=4, column=0, padx=10, pady=5)
entry_RSocial = tk.Entry(root, **entry_style)
entry_RSocial.grid(row=4, column=1, padx=10, pady=5)

label_Cuit = tk.Label(root, text="CUIT", **label_style)
label_Cuit.grid(row=5, column=0, padx=10, pady=5)
entry_Cuit = tk.Entry(root, **entry_style)
entry_Cuit.grid(row=5, column=1, padx=10, pady=5)

label_Neto = tk.Label(root, text="MONTO NETO", **label_style)
label_Neto.grid(row=6, column=0, padx=10, pady=5)
entry_Neto = tk.Entry(root, **entry_style)
entry_Neto.grid(row=6, column=1, padx=10, pady=5)

label_Iva = tk.Label(root, text="IVA", **label_style)
label_Iva.grid(row=7, column=0, padx=10, pady=5)
entry_Iva = tk.Entry(root, **entry_style)
entry_Iva.grid(row=7, column=1, padx=10, pady=5)

label_Total = tk.Label(root, text="TOTAL", **label_style)
label_Total.grid(row=8, column=0, padx=10, pady=5)
entry_Total = tk.Entry(root, **entry_style)
entry_Total.grid(row=8, column=1, padx=10, pady=5)

# Creamos el boton para guardar y crear el archivo .xslx
boton_guardar = tk.Button(root, text="Guardar", command=guardar_datos,
                          bg='#6D8299', fg='white', width=10)
boton_guardar.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()