import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from crud_clientes import abrir_crud_clientes
from crud_productos import abrir_crud_productos
from crud_empleados import abrir_crud_empleados
from crud_pedidos import abrir_crud_pedidos

#funciones de los botones
def abrir_productos():
    messagebox.showinfo("PRODUCTOS", "Abrir CRUD de Productos")

def abrir_categoria():
    messagebox.showinfo("CATEGORÍA", "Abrir CRUD de Categoría")

def abrir_empleados():
    messagebox.showinfo("EMPLEADOS", "Abrir CRUD de Empleados")

def abrir_clientes():
    messagebox.showinfo("CLIENTES", "Abrir CRUD de Clientes")

def abrir_pedidos():
    messagebox.showinfo("PEDIDOS", "Abrir CRUD de Pedidos")

# Ventana principal
ventana = tk.Tk()
ventana.title("LasMiches-ElInge")
ventana.geometry("800x600")
ventana.configure(bg="black")

# Título
titulo = tk.Label(ventana, text="Miches-ElInge", font=("Comic Sans MS", 30, "bold"), fg="RED", bg="black")
titulo.pack(pady=10)

# Frame para botones
botones_frame = tk.Frame(ventana, bg="black")
botones_frame.pack(side="left", padx=50)

# Botones del menú
btn_productos = tk.Button(botones_frame, text="Productos", command=abrir_crud_productos, width=20, height=2, bg="red", fg="white", font=("Arial", 12, "bold"))
btn_productos.pack(pady=10)


btn_empleados = tk.Button(botones_frame, text="Empleados", command=abrir_crud_empleados, width=20, height=2, bg="red", fg="white", font=("Arial", 12, "bold"))
btn_empleados.pack(pady=10)

btn_clientes = tk.Button(botones_frame, text="Clientes", command=abrir_crud_clientes, width=20, height=2, bg="red", fg="white", font=("Arial", 12, "bold"))
btn_clientes.pack(pady=10)

btn_pedidos = tk.Button(botones_frame, text="Pedidos", command=abrir_crud_pedidos, width=20, height=2, bg="red", fg="white", font=("Arial", 12, "bold"))
btn_pedidos.pack(pady=10)


# Cargar la imagen (ajusta tamaño si es necesario)
img = Image.open(r"Miche_imagen.png")
img = img.resize((380, 450))
img_tk = ImageTk.PhotoImage(img)

# Crear un label con la imagen
imagen_label = tk.Label(ventana, image=img_tk, bg="black")
imagen_label.place(x=350, y=100) 

# Mensaje de bienvenida
bienvenido = tk.Label(ventana, text="UNA Y YA", font=("Stencil", 14, "bold"), fg="RED", bg="black")
bienvenido.place(x=350, y=60)

ventana.mainloop()
