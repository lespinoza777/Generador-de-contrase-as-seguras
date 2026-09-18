"""
Aplicación de Escritorio: Generador de Contraseñas Seguras
Descripción: Interfaz gráfica en Tkinter ultra-compatible con Linux/Debian.
Autor: Luis Enrique Espinoza Mieles
"""

import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generar_contrasena():
    """Genera una contraseña segura y la actualiza en la interfaz."""
    try:
        longitud = int(slider.get())
        con_simbolos = var_simbolos.get()
        
        caracteres = string.ascii_letters + string.digits
        if con_simbolos:
            caracteres += string.punctuation
            
        pwd = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, pwd)
        entry.config(state='readonly')
        lbl_status.config(text="")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copiar():
    """Copia la contraseña generada al portapapeles."""
    pwd = entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        lbl_status.config(text="¡Copiado al portapapeles!")
        root.after(2000, lambda: lbl_status.config(text=""))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Credenciales Seguras")
root.geometry("400x360")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Título
tk.Label(root, text="Gestor de Contraseñas", fg="white", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=15)

# Campo de resultado y botón de copiar
frame = tk.Frame(root, bg="#2d2d2d")
frame.pack(pady=5, padx=20, fill="x")

entry = tk.Entry(frame, font=("Courier", 11), fg="#00ffcc", bg="#1e1e1e", justify="center")
entry.pack(side="left", fill="both", expand=True, padx=5, pady=5)
entry.config(state='readonly')

tk.Button(frame, text="Copiar", command=copiar, bg="#007acc", fg="white", cursor="hand2").pack(side="right", padx=5, pady=5)

# Mensaje de estado (Feedback de copiado)
lbl_status = tk.Label(root, text="", fg="#00ffcc", bg="#1e1e1e", font=("Arial", 9))
lbl_status.pack(pady=2)

# Control deslizante (Slider) para la longitud
tk.Label(root, text="Longitud de caracteres (Mín. 8):", fg="white", bg="#1e1e1e", font=("Arial", 10)).pack(anchor="w", padx=20, pady=5)
slider = tk.Scale(root, from_=8, to=32, orient="horizontal", bg="#2d2d2d", fg="white", highlightthickness=0)
slider.set(12)
slider.pack(padx=20, fill="x")

# Checkbox para símbolos
var_simbolos = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Incluir símbolos especiales (!@#$...)", variable=var_simbolos, fg="white", bg="#1e1e1e", selectcolor="#2d2d2d", activebackground="#1e1e1e", activeforeground="white").pack(anchor="w", padx=20, pady=10)

# Botón principal para generar
tk.Button(root, text="Generar Contraseña", command=generar_contrasena, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), cursor="hand2").pack(pady=10, fill="x", padx=20)

# Generar una contraseña inicial al arrancar
generar_contrasena()

# Mantener la app abierta
root.mainloop()