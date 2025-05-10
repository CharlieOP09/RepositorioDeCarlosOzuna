import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_empleados():
    ventana_emp = tk.Toplevel()
    ventana_emp.title("CRUD-Empleados")
    ventana_emp.geometry("700x500")
    ventana_emp.configure(bg="black")

    titulo = tk.Label(ventana_emp, text="EMPLEADOS", font=("Comic Sans MS", 25, "bold"), fg="RED", bg="black")
    titulo.pack(pady=20)

    # Crear empleado
    def crear_empleado():
        nombre = simpledialog.askstring("Crear Empleado", "Nombre del empleado:")
        telefono = simpledialog.askstring("Crear Empleado", "Teléfono:")
        puesto = simpledialog.askstring("Crear Empleado", "Puesto:")
        
        if nombre and telefono and puesto:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO empleados (nombre, telefono, puesto) VALUES (%s, %s, %s)",
                    (nombre, telefono, puesto)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Empleado creado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el empleado.\n{e}")

    # Leer empleados
    def leer_empleado():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT id_empleado, nombre, telefono, puesto FROM empleados")
            empleados = cursor.fetchall()
            conexion.close()

            texto = "\n".join([f"ID: {e[0]} | Nombre: {e[1]} | Tel: {e[2]} | Puesto: {e[3]}" for e in empleados])
            messagebox.showinfo("Empleados Registrados", texto if texto else "No hay empleados registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer la tabla de empleados.\n{e}")

    # Actualizar empleado
    def actualizar_empleado():
        idemp = simpledialog.askinteger("Actualizar Empleado", "ID del empleado a modificar:")
        nuevo_nombre = simpledialog.askstring("Actualizar Empleado", "Nuevo nombre del empleado:")
        nuevo_telefono = simpledialog.askstring("Actualizar Empleado", "Nuevo teléfono:")
        nuevo_puesto = simpledialog.askstring("Actualizar Empleado", "Nuevo puesto:")
        
        if idemp and nuevo_nombre and nuevo_telefono and nuevo_puesto:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE empleados SET nombre=%s, telefono=%s, puesto=%s WHERE id_empleado=%s",
                    (nuevo_nombre, nuevo_telefono, nuevo_puesto, idemp)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el empleado.\n{e}")

    # Eliminar empleado
    def eliminar_empleado():
        idemp = simpledialog.askinteger("Eliminar Empleado", "ID del empleado a eliminar:")
        if idemp:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM empleados WHERE id_empleado=%s", (idemp,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el empleado.\n{e}")

    # Botones del CRUD
    botones = [
        ("Crear", crear_empleado),
        ("Leer", leer_empleado),
        ("Actualizar", actualizar_empleado),
        ("Eliminar", eliminar_empleado),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_emp,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="gray",
            fg="black",
            width=25
        )
        btn.pack(pady=10)

