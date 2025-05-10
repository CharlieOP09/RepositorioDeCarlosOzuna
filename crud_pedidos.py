import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar



def abrir_crud_pedidos():
    ventana_ped = tk.Toplevel()
    ventana_ped.title("CRUD-Pedidos")
    ventana_ped.geometry("700x500")
    ventana_ped.configure(bg="black")

    titulo = tk.Label(ventana_ped, text="PEDIDOS", font=("SComic Sans MS", 25, "bold"), fg="RED", bg="black")
    titulo.pack(pady=20)

    # Crear pedido
    def crear_pedido():
        id_cliente = simpledialog.askinteger("Crear Pedido", "Mesa del cliente: ")
        id_empleado = simpledialog.askinteger("Crear Pedido", "ID del empleado que gestionó el pedido: ")
        total = simpledialog.askfloat("Crear Pedido", "Total del pedido: ")
        estado = simpledialog.askstring("Crear Pedido", "Estado del pedido: ")

        if id_cliente and id_empleado and total and estado:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO pedidos (id_cliente, id_empleado, total, estado) VALUES (%s, %s, %s, %s)",
                    (id_cliente, id_empleado, total, estado)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo(" Éxito", "Pedido creado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el pedido.\n{e}")

    # Leer pedidos
    def leer_pedidos():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.id_pedido, c.nombre, e.nombre, p.fecha, p.total, p.estado 
                FROM pedidos p
                JOIN clientes c ON p.id_cliente = c.id_cliente
                JOIN empleados e ON p.id_empleado = e.id_empleado
            """)
            pedidos = cursor.fetchall()
            conexion.close()

            texto = "\n".join([f"ID: {p[0]} | Cliente: {p[1]} | Empleado: {p[2]} | Fecha: {p[3]} | Total: ${p[4]} | Estado: {p[5]}" for p in pedidos])
            messagebox.showinfo("Pedidos Registrados", texto if texto else "No hay pedidos registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer la tabla de pedidos.\n{e}")

    # Actualizar pedido
    def actualizar_pedido():
        id_pedido = simpledialog.askinteger("Actualizar Pedido", "ID del pedido a modificar:")
        nuevo_estado = simpledialog.askstring("Actualizar Pedido", "Nuevo estado del pedido:")
        nuevo_total = simpledialog.askfloat("Actualizar Pedido", "Nuevo total del pedido:")

        if id_pedido and nuevo_estado and nuevo_total:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE pedidos SET estado=%s, total=%s WHERE id_pedido=%s",
                    (nuevo_estado, nuevo_total, id_pedido)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Pedido actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el pedido.\n{e}")

    # Eliminar pedido
    def eliminar_pedido():
        id_pedido = simpledialog.askinteger("Eliminar Pedido", "ID del pedido a eliminar:")
        if id_pedido:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM pedidos WHERE id_pedido=%s", (id_pedido,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Pedido eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el pedido.\n{e}")

    # Botones del CRUD
    botones = [
        ("Crear", crear_pedido),
        ("Leer", leer_pedidos),
        ("Actualizar", actualizar_pedido),
        ("Eliminar", eliminar_pedido),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_ped,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="gray",
            fg="black",
            width=25
        )
        btn.pack(pady=10)
