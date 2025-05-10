import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_clientes():
    ventana_cli = tk.Toplevel()
    ventana_cli.title("CRUD-Clientes")
    ventana_cli.geometry("700x500")
    ventana_cli.configure(bg="black")

    titulo = tk.Label(ventana_cli, text="CLIENTES", font=("Comic Sans MS", 25, "bold"), fg="RED", bg="black")
    titulo.pack(pady=20)

    # Crear cliente
    def crear_cliente():
        nombre = simpledialog.askstring(" Crear Cliente", "Nombre del cliente:")
        telefono = simpledialog.askstring(" Crear Cliente", "Numero de cliente:")
        preferencias = simpledialog.askstring(" Crear Cliente", "cerveza y sabor del cliente:")

        if nombre and telefono and preferencias:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO clientes (nombre, telefono, preferencias) VALUES (%s, %s, %s)",
                    (nombre, telefono, preferencias)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo(" Éxito", "Cliente creado correctamente.")
            except Exception as e:
                messagebox.showerror(" Error", f"No se pudo crear el cliente.\n{e}")

    # Leer clientes
    def leer_clientes():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT id_cliente, nombre, telefono, preferencias FROM clientes")
            clientes = cursor.fetchall()
            conexion.close()

            texto = "\n".join([f"ID: {c[0]} | Nombre: {c[1]} | Num: {c[2]} | Preferencias: {c[3]}" for c in clientes])
            messagebox.showinfo(" Clientes Registrados", texto if texto else "No hay clientes registrados.")
        except Exception as e:
            messagebox.showerror(" Error", f"No se pudo leer la tabla clientes.\n{e}")

    # Actualizar cliente
    def actualizar_cliente():
        idcli = simpledialog.askinteger(" Actualizar Cliente", "ID del cliente a modificar:")
        nombre = simpledialog.askstring(" Actualizar Cliente", "Nuevo nombre del cliente:")
        telefono = simpledialog.askstring(" Actualizar Cliente", "Nuevo teléfono:")
        preferencias = simpledialog.askstring(" Actualizar Cliente", "Nuevas preferencias:")

        if idcli and nombre and telefono and preferencias:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE clientes SET nombre=%s, telefono=%s, preferencias=%s WHERE id_cliente=%s",
                    (nombre, telefono, preferencias, idcli)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo(" Éxito", "Cliente actualizado correctamente.")
            except Exception as e:
                messagebox.showerror(" Error", f"No se pudo actualizar el cliente.\n{e}")

    # Eliminar cliente
    def eliminar_cliente():
        idcli = simpledialog.askinteger(" Eliminar Cliente", "ID del cliente a eliminar:")
        if idcli:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (idcli,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo(" Éxito", "Cliente eliminado correctamente.")
            except Exception as e:
                messagebox.showerror(" Error", f"No se pudo eliminar el cliente.\n{e}")

    # Botones del CRUD
    botones = [
        (" Crear", crear_cliente),
        (" Leer", leer_clientes),
        (" Actualizar", actualizar_cliente),
        (" Eliminar", eliminar_cliente),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_cli,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="gray",
            fg="black",
            width=25
        )
        btn.pack(pady=10)
