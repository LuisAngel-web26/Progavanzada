import tkinter as tk
from tkinter import messagebox
from backend import *

#Ventanas
ven1=tk.Tk()
ven1.title("Ventana de registro")
ven1.geometry("400x400")

#Etiquetas
label_nombre=tk.Label(ven1, text="Nombre")
label_nombre.pack()

entry_nombre=tk.Entry(ven1,width=40)
entry_nombre.pack(pady=15)

label_edad=tk.Label(ven1,text="Edad")
label_edad.pack()

entry_edad=tk.Entry(ven1,width=40)
entry_edad.pack(pady=15)

label_comida=tk.Label(ven1,text="Comida favorita")
label_comida.pack()

entry_comida=tk.Entry(ven1,width=40)
entry_comida.pack(pady=15)

def registrar():
    name=entry_nombre.get()
    age=entry_edad.get()
    food=entry_comida.get()
    nuevo_usario=Usuario(name,age,food)
    entry_nombre.delete(0,tk.END)
    entry_edad.delete(0,tk.END)
    entry_comida.delete(0,tk.END)
    messagebox.showinfo("Registro del usuario","Tu registro fue exitoso")


boton_registrar= tk.Button(ven1, text="Registrar", command=registrar)
boton_registrar.pack(pady=15)

def mostrar():
    print(Usuario.mostrar_usuarios)





boton_lista= tk.Button(ven1, text="Mostrar lista", command=mostrar)
boton_lista.pack(pady=15)




ven1.mainloop()