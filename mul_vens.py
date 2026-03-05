import tkinter as tk
from PIL import Image, ImageTk

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("800x600")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1, text="El reino animal", bg="lightblue", font=("Arial",23,"bold"))
    eti1.pack()

    frame1=tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen= Image.open("reino_animal.jpg")
    imagen= imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    frame2=tk.Frame(frame1)
    frame2.grid(row=0,column=1,padx=5,pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2, text="Elefante", variable=var, value=1)
    ele.pack()

    jirafa=tk.Radiobutton(frame2, text="Jirafa", variable=var, value=2)
    jirafa.pack()

    castor=tk.Radiobutton(frame2, text="Castor", variable=var, value=3)
    castor.pack()

    leon=tk.Radiobutton(frame2, text="Leon", variable=var, value=4)
    leon.pack()


    def informacion():
        seleccion=var.get()
        if seleccion==1:
               ventana_2()


    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() #Cerrar la segunda ventana
    ventana_principal() #Volver abrir la ventana principal

def ventana_2():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Infomacion de elefante")
    ven2.geometry("700x500")
    ven2.config(bg="gray")

    eti2=tk.Label(ven2, text="Elefante", bg="gray", font=("Algerian",24,"bold"))
    eti2.pack(pady=10)
    frame3=tk.Frame(ven2)
    frame3.pack(fill=tk.X,padx=10,pady=10)
    imagen2= Image.open("elefante.jpg")
    imagen2= imagen2.resize((400,200))
    imagen_tk2= ImageTk.PhotoImage(imagen2)
    label_imagen= tk.Label(frame3, image=imagen_tk2)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)
    Texto1= tk.Label(frame3, text=" El elefante es el mamífero terrestre más grande del planeta, " \
    " perteneciente a la familia Elephantidae y orden Proboscidea. Destaca por su gran tamaño (hasta 8 toneladas)," \
    "largas orejas, colmillos de marfil y una trompa versátil para comer y beber.", wraplength=250, justify="left")
    Texto1.grid(row=0, column=1, padx=5,pady=5)

    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)


    ven2.mainloop()

def ventana_3():
    global ven3
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Esta es mi ventana principal")
    ven3.geometry("500x500")
    ven3.config(bg="green")

    eti1=tk.Label(ven3, text="Aquí estoy viendo la tercera ventana", bg="green")
    eti1.pack(pady=10)
    #Boton para cambiar a ala primera ventana
    boton3=tk.Button(ven3, text="ir a la ventana principal", command=lambda: regresar_a_primera(ven3))
    boton3.pack(pady=30)

    ven3.mainloop()

def ventana_4():
    global ven4
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Esta es mi ventana principal")
    ven4.geometry("500x500")
    ven4.config(bg="red")

    eti1=tk.Label(ven4, text="Aquí estoy viendo la cuarta ventana", bg="red")
    eti1.pack(pady=10)
    #Boton para cambiar a ala primera ventana
    boton3=tk.Button(ven4, text="ir a la ventana principal", command=lambda: regresar_a_primera(ven4))
    boton3.pack(pady=30)

    ven4.mainloop()

def ventana_5():
    global ven4
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Esta es mi ventana principal")
    ven5.geometry("500x500")
    ven5.config(bg="pink")

    eti1=tk.Label(ven5, text="Aquí estoy viendo la quinta ventana", bg="pink")
    eti1.pack(pady=10)
    #Boton para cambiar a ala primera ventana
    boton3=tk.Button(ven5, text="ir a la ventana principal", command=lambda: regresar_a_primera(ven5))
    boton3.pack(pady=30)

    ven5.mainloop()







































ventana_principal()