import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def enviar_nombre():
    nombre=entrada_nombre.get()
    etiqueta_resultado.configure(text=f"Hola,{nombre}")

def salir():
    ventana.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Roxas")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("prueba de ventana")
ventana.geometry("500*300")

menubar= tk.Menu(ventana)

archivo_menu=tk.Menu(menubar,tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="abrir")
archivo_menu.add_command(label="guardar")
archivo_menu.add_separator()
archivo_menu.add_command(label="salir",command=salir)
menubar.add_cascade(label="Archivo",menu=archivo_menu)

editar_menu=tk.Menu(menubar, tearoff=0)
editar_menu.add_command(label="copiar")
editar_menu.add_command(label="pegar")
menubar.add_cascade(label="Editar",menu=editar_menu)

ayuda_menu = tk.Menu(menubar,tearoff=0)
ayuda_menu.add_command(label="Acerca de",command=acerca_de)
menubar.add_cascade(label="Ayuda",menu=ayuda_menu)

ventana.config(menu=menubar)

etiqueta_instruccion=ctk.CTkLabel(ventana,text="introduce tu nombre",font=("Arial",14))
etiqueta_instruccion.pack(pady=20)

entrada_nombre=ctk.CTkEntry(ventana,width=250,font=("Arial",14))
entrada_nombre.pack(pady=10)

boton_enviar=ctk.CTkButton(ventana,text="enviar",command=enviar_nombre,width=150,font=("Arial",14))
boton_enviar.pack(pady=15)

etiqueta_resultado=ctk.CTkLabel(ventana,text="",font=("Arial",16))
etiqueta_resultado.pack(pady=20)

ventana.mainloop()