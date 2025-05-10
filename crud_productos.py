import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_productos():
    ventana_prod = tk.Toplevel()
    ventana_prod.title("CRUD-Productos")
    ventana_prod.geometry("700x500")
    ventana_prod.configure(bg="black")

    titulo = tk.Label(ventana_prod, text="PRODUCTOS", font=("Comic Sans MS", 25, "bold"), fg="RED", bg="black")
    titulo.pack(pady=20)

    # Crear producto
    def crear_producto():
        nombre = simpledialog.askstring("Crear Producto", "Nombre del producto:")
        descripcion = simpledialog.askstring("Crear Producto", "Descripción del producto:")
        precio = simpledialog.askfloat("Crear Producto", "Precio del producto:")
        categoria = simpledialog.askstring("Crear Producto", "Categoría del producto:")
        stock = simpledialog.askinteger("Crear Producto", "Stock disponible:")

        if nombre and descripcion and precio is not None and categoria and stock is not None:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO productos (nombre, descripcion, precio, categoria, stock) VALUES (%s, %s, %s, %s, %s)",
                    (nombre, descripcion, precio, categoria, stock)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Producto creado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el producto.\n{e}")

    # Leer productos
    def leer_productos():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, nombre, descripcion, precio, categoria, stock FROM productos")
            productos = cursor.fetchall()
            conexion.close()

            texto = "\n".join([f"ID: {p[0]} | Nombre: {p[1]} | Desc: {p[2]} | Precio: ${p[3]} | Cat: {p[4]} | Stock: {p[5]}" for p in productos])
            messagebox.showinfo("Productos Registrados", texto if texto else "No hay productos registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer la tabla productos.\n{e}")

    # Actualizar producto
    def actualizar_producto():
        idprod = simpledialog.askinteger("Actualizar Producto", "ID del producto a modificar:")
        nombre = simpledialog.askstring("Actualizar Producto", "Nuevo nombre del producto:")
        descripcion = simpledialog.askstring("Actualizar Producto", "Nueva descripción del producto:")
        precio = simpledialog.askfloat("Actualizar Producto", "Nuevo precio del producto:")
        categoria = simpledialog.askstring("Actualizar Producto", "Nueva categoría del producto:")
        stock = simpledialog.askinteger("Actualizar Producto", "Nuevo stock:")

        if idprod and nombre and descripcion and precio is not None and categoria and stock is not None:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, categoria=%s, stock=%s WHERE id_producto=%s",
                    (nombre, descripcion, precio, categoria, stock, idprod)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el producto.\n{e}")

    # Eliminar producto
    def eliminar_producto():
        idprod = simpledialog.askinteger("Eliminar Producto", "ID del producto a eliminar:")
        if idprod:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM productos WHERE id_producto=%s", (idprod,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el producto.\n{e}")

    # Botones del CRUD
    botones = [
        ("Crear", crear_producto),
        ("Leer", leer_productos),
        ("Actualizar", actualizar_producto),
        ("Eliminar", eliminar_producto),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_prod,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="gray",
            fg="black",
            width=25
        )
        btn.pack(pady=10)
