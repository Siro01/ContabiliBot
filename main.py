import tkinter as tk
from tkinter import messagebox

# Interfaz de usuario con tkinter
root = tk.Tk()
root.title("ContabiliBot")
root.geometry("800x600")

screen_width = root.winfo_screenwidth() # Ancho de pantalla
screen_height = root.winfo_screenheight() # Alto de pantalla
window_width = 800
window_height = 600

# Calcular la posicion x, y para centrar
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Configurar tamanio y posicion
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Evito que se cambie el ancho y alto
root.resizable(False, False)

#Estilos
root.configure(bg='#4B6587')
label_style = {"bg": '#4B6587', "fg": "white"}
entry_style = {"bg": '#D3D3D3', "fg": "black"}

# Botones de la interfaz
boton = tk.Button(root, text="Importar", width=15, height=2)
boton.place(x=50, y=200)

boton2 = tk.Button(root, text="Exportar", width=15, height=2)
boton2.place(x=650, y=200)

boton3 = tk.Button(root, text="Copiar y pegar", width=15, height=2)
boton3.place(x=300, y=300)



root.mainloop()