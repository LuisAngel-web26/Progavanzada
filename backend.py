import csv

class Usuario():
    lista=[]
    def __init__(self,name,age,food):
        self.nombre=name
        self.edad=age
        self.comida=food
        if self not in Usuario.lista:
            Usuario.lista.append(self)
    
    def mostrar_info(self):
        return f"EL usuario {self.nombre} tiene {self.edad} y le gusta {self.comida}"
    
    @classmethod
    def mostrar_usuarios(cls):
        return cls.lista
    
    @classmethod
    def guardar_usarios():
        campos=["edad","edad","comida"]
        with open("personas.csv","w",encoding="utf-8") as f:
            escritor=csv.DictWriter(f,fieldnames=campos)
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"comida":u.comida})